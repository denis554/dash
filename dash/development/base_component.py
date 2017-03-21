import collections
import copy
import sys
import types


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


class Component(collections.MutableMapping):
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            if k not in self._prop_names:
                # TODO - What's the right exception here?
                raise Exception(
                    'Unexpected keyword argument `{}`'.format(k) +
                    '\nAllowed arguments: {}'.format(
                        ', '.join(self._prop_names)
                    )
                )
            setattr(self, k, v)

    def to_plotly_json(self):
        as_json = {
            'props': {p: getattr(self, p)
                      for p in self._prop_names
                      if hasattr(self, p)},
            'type': self._type,
            'namespace': self._namespace
        }

        return as_json

    def _check_if_has_indexable_content(self, item):
        if (not hasattr(item, 'content') or
                (not isinstance(item.content, Component) and
                 not isinstance(item.content, collections.MutableSequence))):

            raise KeyError

    def _get_set_or_delete(self, id, operation, new_item=None):
        self._check_if_has_indexable_content(self)

        if isinstance(self.content, Component):
            if getattr(self.content, 'id', None) is not None:
                # Woohoo! It's the item that we're looking for
                if self.content.id == id:
                    if operation == 'get':
                        return self.content
                    elif operation == 'set':
                        self.content = new_item
                        return
                    elif operation == 'delete':
                        self.content = None
                        return

            # Recursively dig into its subtree
            try:
                if operation == 'get':
                    return self.content.__getitem__(id)
                elif operation == 'set':
                    self.content.__setitem__(id, new_item)
                    return
                elif operation == 'delete':
                    self.content.__delitem__(id)
                    return
            except KeyError:
                pass

        # if content is like a list
        if isinstance(self.content, collections.MutableSequence):
            for (i, item) in enumerate(self.content):
                # If the item itself is the one we're looking for
                if getattr(item, 'id', None) == id:
                    if operation == 'get':
                        return item
                    elif operation == 'set':
                        self.content[i] = new_item
                        return
                    elif operation == 'delete':
                        del self.content[i]
                        return

                # Otherwise, recursively dig into that item's subtree
                # Make sure it's not like a string
                elif isinstance(item, Component):
                    try:
                        if operation == 'get':
                            return item.__getitem__(id)
                        elif operation == 'set':
                            item.__setitem__(id, new_item)
                            return
                        elif operation == 'delete':
                            item.__delitem__(id)
                            return
                    except KeyError:
                        pass

        # The end of our branch
        # If we were in a list, then this exception will get caught
        raise KeyError

    # Supply ABC methods for a MutableMapping:
    # - __getitem__
    # - __setitem__
    # - __delitem__
    # - __iter__
    # - __len__

    def __getitem__(self, id):
        '''Recursively find the element with the given ID through the tree
        of content.
        '''
        # TODO - Rename content to children
        # A component's content can be undefined, a string, another component,
        # or a list of components.
        return self._get_set_or_delete(id, 'get')

    def __setitem__(self, id, item):
        '''Set an element by its ID
        '''
        return self._get_set_or_delete(id, 'set', item)

    def __delitem__(self, id):
        '''Delete items by ID in the tree of content
        '''
        return self._get_set_or_delete(id, 'delete')


    def traverse(self):
        '''Yield each item in the tree'''
        content = getattr(self, 'content', None)

        # content is just a component
        if isinstance(content, Component):
            yield content
            for t in content.traverse():
                yield t

        # content is a list of components
        elif isinstance(content, collections.MutableSequence):
            for i in content:
                yield i

                if isinstance(i, Component):
                    for t in i.traverse():
                        yield t

    def __iter__(self):
        '''Yield IDs in the tree of content
        '''
        for t in self.traverse():
            if (isinstance(t, Component) and
                getattr(t, 'id', None) is not None):

                yield t.id


    def __len__(self):
        '''Return the number of items in the tree
        '''
        # TODO - Should we return the number of items that have IDs
        # or just the number of items?
        # The number of items is more intuitive but returning the number
        # of IDs matches __iter__ better.
        length = 0
        if getattr(self, 'content', None) is None:
            length = 0
        elif isinstance(self.content, Component):
            length = 1
            length += len(self.content)
        elif isinstance(self.content, collections.MutableSequence):
            for c in self.content:
                length += 1
                if isinstance(c, Component):
                    length += len(c)
        else:
            # string or number
            length = 1
        return length


def generate_class(typename, props, description, namespace):
    # Dynamically generate classes to have nicely formatted docstrings,
    # keyword arguments, and repr
    # Insired by http://jameso.be/2013/08/06/namedtuple.html

    # TODO - Tab out the repr for the repr of these components to make it
    # look more like a heirarchical tree
    # TODO - Include "description" "defaultValue" in the repr and docstring
    #
    # TODO - Handle "required"
    #
    # TODO - How to handle user-given `null` values? I want to include
    # an expanded docstring like Dropdown(value=None, id=None)
    # but by templating in those None values, I have no way of knowing
    # whether a property is None because the user explicitly wanted
    # it to be `null` or whether that was just the default value.
    # The solution might be to deal with default values better although
    # not all component authors will supply those.
    c = '''class {typename}(Component):
        """{docstring}
        """
        def __init__(self, {default_argtext}):
            self._prop_names = {list_of_valid_keys}
            self._type = '{typename}'
            self._namespace = '{namespace}'
            super({typename}, self).__init__({argtext})

        def __repr__(self):
            if(any(getattr(self, c, None) is not None for c in self._prop_names
                   if c is not self._prop_names[0])):

                return '{typename}('+', '.join([c+'='+repr(getattr(self, c, None))
                                                for c in self._prop_names if getattr(self, c, None) is not None])+')'

            else:
                return '{typename}(' + repr(getattr(self, self._prop_names[0], None)) + ')'
    '''
    list_of_valid_keys = repr(props.keys())
    bullet_list_of_valid_keys = ('- ' + '\n- '.join(
        list_of_valid_keys
    ))

    if 'content' in component_arguments:
        default_argtext = 'content=None, **kwargs'
        argtext = 'content=content, **kwargs'
    else:
        default_argtext = '**kwargs'
        argtext = '**kwargs'

    d = c.format(**locals())

    scope = {'Component': Component}
    exec d in scope
    result = scope[typename]
    return result

def create_docstring(name, props, description):
    if 'content' in props:
        props = collections.OrderedDict(
            [['content', props.pop('content')]] +
            zip(props.keys(), props.values())
        )
    return '''A {name} component.{description}

    Keyword arguments:
    {args}

    '''.format(
        name=name,
        description='\n{}'.format(description),
        args='\n'.join(
            ['- {}'.format(argument_doc(
                p, prop['type'], prop['required'], prop['description']
            )) for p, prop in filter_props(props).iteritems()]
        )
    ).replace('    ', '')

def filter_props(args):
    filtered_args = copy.deepcopy(args)
    for arg_name in filtered_args:
        arg_type =  args[arg_name]['type']['name']
        if arg_type in ['func', 'symbol', 'instanceOf']:
            filtered_args.pop(arg_name)
    return filtered_args

def js_to_py_type(type_object):
    js_type_name = type_object['name']

    js_to_py_types = {
        'array': lambda: 'list',
        'bool': lambda: 'boolean',
        'number': lambda: 'number',
        'string': lambda: 'string',
        'object': lambda: 'dict',

        'any': lambda: 'boolean | number | string | dict | list',
        'element': lambda: 'dash component',
        'node': lambda: (
            'a list of or a singular dash component, string or number'
        ),

        # React's PropTypes.oneOf
        'enum': lambda: 'a value equal to: {}'.format(', '.join([
            '{}'.format(str(t['value'])) for t in type_object['value']
        ])),

        # React's PropTypes.oneOfType
        'union': lambda: '{}'.format(' | '.join([
            '{}'.format(js_to_py_type(subType))
            for subType in type_object['value'] if js_to_py_type(subType) != ''
        ])),

        # React's PropTypes.arrayOf
        'arrayOf': lambda: 'list'.format(
            'of {}s'.format(js_to_py_type(type_object['value']))
            if js_to_py_type(type_object['value']) != ''
            else ''
        ),

        # React's PropTypes.objectOf
        'objectOf': lambda: (
            'dict with strings as keys and values of type {}'
        ).format(js_to_py_type(type_object['value'])),

        # React's PropTypes.shape
        'shape': lambda: (
            'dict containing keys {}.\n{}'.format(
                ', '.join(
                    ["'{}'".format(t) for t in type_object['value'].keys()]
                ),
                'Those keys have the following types: \n{}'.format(
                    '\n'.join([
                        '  - ' + argument_doc(
                            prop_name,
                            prop,
                            prop['required'],
                            prop.get('description', '')
                        ) for
                        prop_name, prop in type_object['value'].iteritems()
                    ])
                )
            )
        )

    }
    if 'computed' in type_object and type_object['computed']:
        return ''
    if js_type_name in js_to_py_types:
        return js_to_py_types[js_type_name]()
    else:
        return ''

def argument_doc(arg_name, type_object, required, description):
    js_type_name = type_object['name']
    py_type_name = js_to_py_type(type_object)
    if '\n' in py_type_name:
        return (
            '{name} ({is_required}): {description}. '
            '{name} has the following type: {type}'
        ).format(
            name=arg_name,
            type=py_type_name,
            description=description,
            is_required='required' if required else 'optional'
        )

    else:
        return '{name} ({type}{is_required}){description}'.format(
            name=arg_name,
            type='{}; '.format(py_type_name) if py_type_name else '',
            description=': {}'.format(description) if description != '' else '',
            is_required='required' if required else 'optional'
        )

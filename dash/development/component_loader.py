from base_component import generate_class
import collections
import json


def load_components(metadata_path,
                    namespace='default_namespace'):
    """Load React component metadata into a format Dash can parse.

    Usage: load_components('../../component-suites/lib/metadata.json', ['content', 'id', 'key', 'className', 'style', 'dependencies'])

    Keyword arguments:
    metadata_path -- a path to a JSON file created by [`react-docgen`](https://github.com/reactjs/react-docgen).
    default_props -- props not in component propTypes that should be considered valid.

    Returns:
    components -- a list of component objects with keys `type`, `valid_kwargs`, and `setup`.
    """

    # This will be returned
    components = []

    # Start processing
    with open(metadata_path) as data_file:
        json_string = data_file.read()
        data = json\
            .JSONDecoder(object_pairs_hook=collections.OrderedDict)\
            .decode(json_string)

    # Iterate over each property name (which is a path to the component)
    for componentPath in data:
        componentData = data[componentPath]

        # Extract component name from path
        # e.g. src/components/MyControl.react.js
        # TODO Make more robust - some folks will write .jsx and others
        # will be on windows. Unfortunately react-docgen doesn't include
        # the name of the component atm.
        name = componentPath.split('/').pop().split('.')[0]

        # If "content" is a prop, then move it to the front to respect
        # dash convention
        props = componentData['props']
        if 'content' in props:
            props = OrderedDict(
                [('content', props.pop('content'), )] +
                zip(props.keys(), props.values())
            )

        component = generate_class(
            name,
            props,
            description,
            namespace
        )

        # TODO - Remove this
        # scope[component_spec['type']] = component
        components.append(component)

    return components

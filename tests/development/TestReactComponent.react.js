import React from 'react';
// A react component with all of the available proptypes to run tests over

/**
 * This is a description of the component.
 * It's multiple lines long.
 */
class ReactComponent extends Component {
    render() {
        return '';
    }
}

ReactComponent.propTypes = {
    /**
     * Description of optionalArray
     */
    optionalArray: React.PropTypes.array,
    optionalBool: React.PropTypes.bool,
    optionalFunc: React.PropTypes.func,
    optionalNumber: React.PropTypes.number,
    optionalObject: React.PropTypes.object,
    optionalString: React.PropTypes.string,
    optionalSymbol: React.PropTypes.symbol,

    content: React.PropTypes.node,

    // Anything that can be rendered: numbers, strings, elements or an array
    // (or fragment) containing these types.
    optionalNode: React.PropTypes.node,

    // A React element.
    optionalElement: React.PropTypes.element,

    // You can also declare that a prop is an instance of a class. This uses
    // JS's instanceof operator.
    optionalMessage: React.PropTypes.instanceOf(Message),

    // You can ensure that your prop is limited to specific values by treating
    // it as an enum.
    optionalEnum: React.PropTypes.oneOf(['News', 'Photos']),

    // An object that could be one of many types
    optionalUnion: React.PropTypes.oneOfType([
        React.PropTypes.string,
        React.PropTypes.number,
        React.PropTypes.instanceOf(Message)
    ]),

    // An array of a certain type
    optionalArrayOf: React.PropTypes.arrayOf(React.PropTypes.number),

    // An object with property values of a certain type
    optionalObjectOf: React.PropTypes.objectOf(React.PropTypes.number),

    // An object taking on a particular shape
    optionalObjectWithShapeAndNestedDescription: React.PropTypes.shape({
        color: React.PropTypes.string,
        fontSize: React.PropTypes.number,
        /**
         * Figure is a plotly graph object
         */
        figure: React.PropTypes.shape({
            /**
             * data is a collection of traces
             */
            data: React.PropTypes.arrayOf(React.PropTypes.object),
            /**
             * layout describes the rest of the figure
             */
            layout: React.PropTypes.object
        })
    }),

    // You can chain any of the above with `isRequired` to make sure a warning
    // is shown if the prop isn't provided.
    requiredFunc: React.PropTypes.func.isRequired,

    // A value of any data type
    requiredAny: React.PropTypes.any.isRequired,

    requiredArray: React.PropTypes.array.isRequired,

    customProp: function(props, propName, componentName) {
        if (!/matchme/.test(props[propName])) {
            return new Error(
            'Invalid prop `' + propName + '` supplied to' +
            ' `' + componentName + '`. Validation failed.'
            );
        }
    },

    customArrayProp: React.PropTypes.arrayOf(function(propValue, key, componentName, location, propFullName) {
        if (!/matchme/.test(propValue[key])) {
            return new Error(
            'Invalid prop `' + propFullName + '` supplied to' +
            ' `' + componentName + '`. Validation failed.'
            );
        }
    })
};

ReactComponent.defaultProps = {
    optionalNumber: 42,
    optionalString: 'hello world'
};

export default ReactComponent;

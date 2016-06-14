'use strict';

import React, { Component } from 'react';
import { DragSource } from 'react-dnd';

const style = {
    border: '1px dashed blue'
};

const beginDrag = (props) => ({name: props.name});

const endDrag = (props, monitor)  => {
    if (!monitor.didDrop()) return;

    const thisItem = monitor.getItem();
    const dropResult = monitor.getDropResult();

    if (dropResult) {
        console.log( // eslint-disable-line no-console
            `you dropped ${thisItem.name} into ${dropResult.name}`
        );
    }
}

const collectProps = (connect, monitor) => ({
    connectDragSource: connect.dragSource(),
    isDragging: monitor.isDragging()
});

export class Draggable extends Component {
    render() {
        console.warn('Draggable: ', this.props); // eslint-disable-line
        const { isDragging, connectDragSource } = this.props;
        return connectDragSource(
            isDragging ?
                <div style={style}>{this.props.children}</div>
                :
                <div>{this.props.children}</div>
        );
    }
}

export default DragSource('Draggable', {beginDrag, endDrag}, collectProps)(Draggable);

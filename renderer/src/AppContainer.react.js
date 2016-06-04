import React from 'react';
import {Provider} from 'react-redux'

import initializeStore from './store';
import TreeContainer from './TreeContainer.react';

const store = initializeStore();

export default () => (
    <Provider store={store}>
        <TreeContainer/>
    </Provider>
);


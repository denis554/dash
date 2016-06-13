import spec from '../spec'; // TODO: this'll eventually load from the API
import {crawlLayout, createTreePath} from './utils'

const initialPaths = {};

// TODO: Don't initialize path map as side-effect of importing reducer.
crawlLayout(spec, (child, itempath) => {
    if(child.props && child.props.id) {
        initialPaths[child.props.id] = createTreePath(itempath);
    }
});

const paths = (state = initialPaths, action) => {
    switch (action.type) {
        default:
            return state;
    }
}

export default paths;

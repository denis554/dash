// TODO `state` should be an ImmutableJS data structure
const requestQueue = (state = [], action) => {
    switch (action.type) {
        case 'SET_REQUEST_QUEUE':
            console.warn(`REQUEST QUEUE ${action.payload}`); // eslint-disable-line
            if (Array.isArray(action.payload)) {
                state = Object.assign({}, action.payload);
            }

            return state;

        default:
            return state;
    }
}

export default requestQueue;

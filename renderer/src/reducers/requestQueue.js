const requestQueue = (state = [], action) => {
    switch (action.type) {
        case 'SET_REQUEST_QUEUE':
            if (Array.isArray(action.payload)) {
                state = Object.assign({}, action.payload);
            }

            return state;

        default:
            return state;
    }
}

export default requestQueue;

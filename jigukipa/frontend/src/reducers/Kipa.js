import { GET_POST } from "../actions/types";

const initialState = {
  Posts: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_POST:
      return {
        ...state,
        Posts: action.payload,
      };
    default:
      return state;
  }
}

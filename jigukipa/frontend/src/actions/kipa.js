import axios from 'axios';

import { GET_POST } from './types';


export const getPosts = () => (dispatch) => {
  
    axios
      .get('/api/post/')
      .then((res) => {
        dispatch({
          type: GET_POST,
          payload: res.data,
        });
      })
      .catch((err) =>
        console.log(err)
      );
  };
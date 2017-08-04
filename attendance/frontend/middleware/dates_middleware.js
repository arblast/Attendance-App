import {CREATE_DATE, FETCH_DATE, receiveAttendees} from '../actions/dates_actions.js';
import {fetchDate, createDate} from '../util/dates_api_util.js';

const DateMiddleware = store => next => action => {
  let success = (data) => store.dispatch(receiveAttendees(data.attendees));
  let error = (data) => console.log(error);
  switch(action.type) {
    case CREATE_DATE:
      createDate(action.dateParams, success, error);
      return next(action);
    case FETCH_DATE:
      fetchDate(success, error);
      return next(action);
    default:
      return next(action);
  }
}

export default DateMiddleware;

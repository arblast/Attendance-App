import {CREATE_DATE, FETCH_DATE} from '../actions/dates_actions.js';
import {receiveAttendees} from '../actions/attendees_actions.js';
import {fetchDate, createDate} from '../util/dates_api_util.js';

const DateMiddleware = store => next => action => {
  let success = (data) => store.dispatch(receiveAttendees(data.attendees));
  let error = (data) => console.log(data);
  switch(action.type) {
    case CREATE_DATE:
      createDate(action.dateParams, success, error);
      return next(action);
    case FETCH_DATE:
      fetchDate(action.dateParams, success, error);
      return next(action);
    default:
      return next(action);
  }
}

export default DateMiddleware;

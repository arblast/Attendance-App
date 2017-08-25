import { applyMiddleware } from 'redux';
import AttendeeMiddleware from './attendees_middleware.js';
import DateMiddleware from './dates_middleware.js';

export default applyMiddleware(
  AttendeeMiddleware,
  DateMiddleware
);

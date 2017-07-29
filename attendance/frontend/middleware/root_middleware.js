import { applyMiddleware } from 'redux';
import AttendeeMiddleware from './attendees_middleware.js';

export default applyMiddleware(
  AttendeeMiddleware
);

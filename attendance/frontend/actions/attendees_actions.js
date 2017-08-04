export const CREATE_ATTENDEE = "CREATE_ATTENDEE";
export const FETCH_ATTENDEES = "FETCH_ATTENDEES";
export const RECEIVE_ATTENDEES = "RECEIVE_ATTENDEES";
export const CREATE_DATE = "CREATE_DATE";
export const FETCH_DATE = "FETCH_DATE";

export const createAttendee = (attendeeParams) => ({
  type: CREATE_ATTENDEE,
  attendeeParams
});

export const fetchAttendees = () => ({
  type: FETCH_ATTENDEES,
});

export const receiveAttendees = (attendees) => ({
  type: RECEIVE_ATTENDEES,
  attendees
});

export const createDate = (dateParams) => ({
  type: CREATE_DATE,
  dateParams
});

export const fetchDate = (dateParams) => ({
  type: FETCH_DATE,
  dateParams
});

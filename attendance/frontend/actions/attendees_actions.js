export const CREATE_ATTENDEE = "CREATE_ATTENDEE";
export const FETCH_ATTENDEES = "FETCH_ATTENDEES";
export const RECEIVE_ATTENDEES = "RECEIVE_ATTENDEES"

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

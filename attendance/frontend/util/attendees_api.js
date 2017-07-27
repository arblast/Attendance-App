export const fetchAttendees = (success, error) => {
  $.ajax({
    type: "GET",
    url: "/attendanceapp/attendee/",
    success,
    error
  });
};

export const createAttendee = (attendeeParams, success, error) => {
  $.ajax({
    type: "POST",
    data: attendeeParams,
    url: "/attendanceapp/attendee/",
    success,
    error
  });
}

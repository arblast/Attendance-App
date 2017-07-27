export const fetchAttendees = (success, error) => {
  $.ajax({
    type: "GET",
    url: "/attendanceapp/attendee/",
    success,
    error
  });
};

export const createAttendee = (attendeeParams, token, success, error) => {
  $.ajax({
    type: "POST",
    headers: {'X-CSRFToken': token},
    data: attendeeParams,
    url: "/attendanceapp/attendee/",
    success,
    error
  });
}

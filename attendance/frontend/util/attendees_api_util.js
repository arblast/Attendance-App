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
    headers: {'X-CSRFToken': attendeeParams.token},
    data: attendeeParams.params,
    url: "/attendanceapp/attendee/",
    success,
    error
  });
}

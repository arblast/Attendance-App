export const fetchAttendees = (success, error) => {
  $.ajax({
    type: "GET",
    url: "/attendanceapp/attendee/",
    success,
    error
  });
};

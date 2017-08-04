export const createDate = (dateParams, token, success, error) => {
  $.ajax({
    type: "POST",
    headers: {'X-CSRFToken': token},
    data: dateParams,
    url: "/attendanceapp/date/",
    success,
    error
  });
}

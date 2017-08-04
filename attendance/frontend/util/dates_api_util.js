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

export const fetchDate = (dateParams, success, error) => {
  $.ajax({
    type: "GET",
    data: dateParams,
    url: "/attendanceapp/date/",
    success,
    error
  });
};

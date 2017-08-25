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
  let year = dateParams.year;
  let month = dateParams.month;
  let day = dateParams.day;
  $.ajax({
    type: "GET",
    url: `/attendanceapp/date/${year}/${month}/${day}`,
    success,
    error
  });
};

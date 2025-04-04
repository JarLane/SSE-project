
pingfunc(str addr)

realresponse = ping(addr)
response = extractcode(realresponse)
if (response != 200) {
  if (errorcode == response) {
   if (increment $ 4 == 0) {
      increment++
      Archive(realresponse)
      }
    increment++
    return
  } else {
    errorcode = response
    increment = 0
    archive(realresponse)
  }
} elif ( errorcode != 200) {
  errorcode = 0
  Archive("All issues resolved")
} else {
  return
}


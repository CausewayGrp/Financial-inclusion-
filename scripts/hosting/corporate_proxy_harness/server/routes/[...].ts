// The corporate site's own pages: anything the forwarding middleware does not take answers here.
import { defineEventHandler, setResponseStatus } from 'h3'
export default defineEventHandler((event) => {
  setResponseStatus(event, 404)
  return 'corporate site: not found'
})

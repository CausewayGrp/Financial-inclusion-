// The corporate site's behaviour observed on 3 October 2026 (docs/RELEASE_RUNBOOK.md, "Hosting"): every response,
// its own 404 for this path included, carries a `session` cookie on Path=/, `x-robots-tag` and `x-powered-by: Nuxt`.
// Here they are set by a server middleware that runs before the forwarding middleware, i.e. inside Nitro, before
// routing. That is the case the forwarding middleware can clean. A header added by a server in front of Nitro (an nginx
// or a load balancer on the Droplet) is NOT simulated here and cannot be removed by the middleware: the runbook's
// web-administrator check (step 8) establishes where these headers originate.
import { defineEventHandler, setCookie, setHeader } from 'h3'
export default defineEventHandler((event) => {
  setCookie(event, 'session', 'corporate-session-value', { path: '/' })
  setHeader(event, 'x-robots-tag', 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1')
  setHeader(event, 'x-powered-by', 'Nuxt')
})

// A stand-in for CauseWay's corporate Nuxt/Nitro server, used only by scripts/tests/test_corporate_proxy.py
// (R-09, independent review of 70398d1). Not deployed anywhere.
// srcDir 'server': the folder layout of a Nuxt application, where the forwarding middleware is written.
export default defineNitroConfig({ compatibilityDate: '2025-01-01', srcDir: 'server' })

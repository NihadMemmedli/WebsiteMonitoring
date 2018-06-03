# WebsiteMonitoring

1. Reads a list of web pages (HTTP URLs) and corresponding page content requirements from
a configuration file.
2. Periodically makes an HTTP request to each page.
3. Verifies that the page content received from the server matches the content requirements.
4. Measures the time it took for the web server to complete the whole request.
5. Writes a log file that shows the progress of the periodic checks.
6. Implement a single-page HTTP server interface in the same process that shows (HTML) each
monitored web site and their current (last check) status.

Details:
• The “content requirement” can for example be just a simple string that must be included in the
response received from the server, e.g. one rule might be that the page at the URL
“http://www.foobar.com/login” must contain the text “Please login:”.
• The checking period configurable by a setting in the
configuration file.(config.config.py)
• The log file must contain the checked URLs, their status and the response times. (logs folder)
• The program must distinguish between connection level problems (e.g. the web site is down)
and content problems (e.g. the content requirements were not fulfilled). (log file or report file show difference)

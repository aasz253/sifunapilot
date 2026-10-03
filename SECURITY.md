# Security Policy

## Reporting Security Issues

Please report security vulnerabilities to the maintainers privately.

## Security Principles

SifunaPilot is designed with security as a core principle:

1. **Local-first**: Minimize cloud exposure by default
2. **Permission-based**: All sensitive actions require appropriate permissions
3. **Confirmation required**: Destructive or sensitive operations require user confirmation
4. **No credential leakage**: Credentials are never exposed to AI models
5. **Untrusted content isolation**: Web content is treated as untrusted data, not system instructions
6. **Minimal logging**: Sensitive data (passwords, keys, tokens) is never logged
7. **Defense in depth**: Multiple security layers

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Security Boundaries

- Never bypass authentication, CAPTCHA, or security controls
- Never execute dangerous commands without explicit permission
- Never silently delete user data or perform financial transactions
- Treat all external content (web pages) as potentially malicious

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class EmailService:
    """Email service for sending OTP and notifications"""
    
    def __init__(self):
        # Email configuration from environment
        self.smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        self.smtp_port = int(os.getenv("SMTP_PORT", 587))
        self.smtp_user = os.getenv("SMTP_USER")
        self.smtp_password = os.getenv("SMTP_PASSWORD")
        self.from_email = os.getenv("FROM_EMAIL", self.smtp_user)
        self.from_name = os.getenv("FROM_NAME", "YogKulam")
    
    def send_email(
        self, 
        to_email: str, 
        subject: str, 
        html_content: str,
        text_content: Optional[str] = None
    ) -> bool:
        """
        Send an email
        Args:
            to_email: Recipient email
            subject: Email subject
            html_content: HTML email body
            text_content: Plain text fallback (optional)
        Returns:
            True if sent successfully, False otherwise
        """
        try:
            # Create message
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = f"{self.from_name} <{self.from_email}>"
            message["To"] = to_email
            
            # Add plain text version (fallback)
            if text_content:
                part1 = MIMEText(text_content, "plain")
                message.attach(part1)
            
            # Add HTML version
            part2 = MIMEText(html_content, "html")
            message.attach(part2)
            
            # Send email
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()  # Enable TLS
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(message)
            
            print(f"✅ Email sent successfully to {to_email}")
            return True
            
        except Exception as e:
            print(f"❌ Error sending email to {to_email}: {e}")
            return False
    
    def send_verification_otp(self, to_email: str, otp: str, user_name: Optional[str] = None) -> bool:
        """Send email verification OTP - YogKulam Style"""
        
        greeting = f"Hi {user_name.split()[0] if user_name else 'there'},"
        
        subject = "Welcome to YogKulam!"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    background-color: #f5f5f5;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #ffffff;
                }}
                .header {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 40px 30px;
                    text-align: center;
                }}
                .header h1 {{
                    margin: 0;
                    color: #ffffff;
                    font-size: 28px;
                    font-weight: 600;
                }}
                .header p {{
                    margin: 10px 0 0 0;
                    color: #ffffff;
                    font-size: 16px;
                    opacity: 0.95;
                }}
                .content {{
                    padding: 40px 30px;
                }}
                .greeting {{
                    font-size: 16px;
                    color: #333333;
                    margin-bottom: 15px;
                }}
                .message {{
                    font-size: 15px;
                    color: #555555;
                    line-height: 1.6;
                    margin-bottom: 20px;
                }}
                .otp-section {{
                    background-color: #f8f9fa;
                    border: 2px dashed #667eea;
                    border-radius: 8px;
                    padding: 30px;
                    text-align: center;
                    margin: 30px 0;
                }}
                .otp-label {{
                    font-size: 14px;
                    color: #666666;
                    margin-bottom: 10px;
                }}
                .otp-code {{
                    font-size: 36px;
                    font-weight: 700;
                    color: #667eea;
                    letter-spacing: 8px;
                    font-family: 'Courier New', monospace;
                    margin: 10px 0;
                }}
                .otp-instruction {{
                    font-size: 13px;
                    color: #666666;
                    margin-top: 10px;
                }}
                .warning-box {{
                    background-color: #fff8e1;
                    border-left: 4px solid #ffc107;
                    padding: 15px;
                    margin: 20px 0;
                    border-radius: 4px;
                }}
                .warning-box p {{
                    margin: 0;
                    font-size: 13px;
                    color: #856404;
                }}
                .warning-icon {{
                    font-size: 16px;
                    margin-right: 5px;
                }}
                .benefits {{
                    margin: 25px 0;
                }}
                .benefit-item {{
                    display: flex;
                    align-items: flex-start;
                    margin: 12px 0;
                    font-size: 14px;
                    color: #555555;
                }}
                .benefit-icon {{
                    margin-right: 10px;
                    font-size: 18px;
                }}
                .footer {{
                    text-align: center;
                    padding: 30px;
                    background-color: #f8f9fa;
                    border-top: 1px solid #e9ecef;
                }}
                .footer-text {{
                    font-size: 13px;
                    color: #6c757d;
                    margin: 5px 0;
                }}
                .disclaimer {{
                    font-size: 12px;
                    color: #999999;
                    margin-top: 20px;
                    line-height: 1.5;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <h1>🧘 Welcome to YogKulam!</h1>
                    <p>Just one more step to complete your registration</p>
                </div>
                
                <div class="content">
                    <p class="greeting">{greeting}</p>
                    
                    <p class="message">
                        Welcome to YogKulam! We're excited to have you join our yoga community.
                    </p>
                    
                    <p class="message">
                        To complete your registration and verify your email address, please enter the verification code below:
                    </p>
                    
                    <div class="otp-section">
                        <div class="otp-label">Your Verification Code</div>
                        <div class="otp-code">{otp}</div>
                        <div class="otp-instruction">Enter this code to verify your account</div>
                    </div>
                    
                    <div class="warning-box">
                        <p><span class="warning-icon">⚠️</span> <strong>Important:</strong> This code will expire in <strong>5 minutes</strong>. If you don't verify within this time, you'll need to request a new code.</p>
                    </div>
                    
                    <p class="message">Once verified, you'll be able to:</p>
                    
                    <div class="benefits">
                        <div class="benefit-item">
                            <span class="benefit-icon">🧘</span>
                            <span>Access guided yoga sessions</span>
                        </div>
                        <div class="benefit-item">
                            <span class="benefit-icon">📅</span>
                            <span>Schedule your practice sessions</span>
                        </div>
                        <div class="benefit-item">
                            <span class="benefit-icon">👥</span>
                            <span>Connect with our yoga community</span>
                        </div>
                        <div class="benefit-item">
                            <span class="benefit-icon">📊</span>
                            <span>Track your progress and achievements</span>
                        </div>
                    </div>
                    
                    <p class="disclaimer">
                        If you didn't create this account, please ignore this email and the account will not be activated.
                    </p>
                </div>
                
                <div class="footer">
                    <p class="footer-text"><strong>Namaste,</strong></p>
                    <p class="footer-text">The YogKulam Team</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        text_content = f"""
        Hi {user_name.split()[0] if user_name else 'there'},
        
        Welcome to YogKulam! We're excited to have you join our yoga community.
        
        Your verification code is: {otp}
        
        This code will expire in 5 minutes.
        
        If you didn't create this account, please ignore this email.
        
        Namaste,
        The YogKulam Team
        """
        
        return self.send_email(to_email, subject, html_content, text_content)
    
    def send_password_reset_otp(self, to_email: str, otp: str, user_name: Optional[str] = None) -> bool:
        """Send password reset OTP - YogKulam Style"""
        
        greeting = f"Hi {user_name.split()[0] if user_name else 'there'},"
        
        subject = "Password Reset Request - YogKulam"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    background-color: #f5f5f5;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #ffffff;
                }}
                .header {{
                    background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
                    padding: 40px 30px;
                    text-align: center;
                }}
                .header h1 {{
                    margin: 0;
                    color: #ffffff;
                    font-size: 28px;
                    font-weight: 600;
                }}
                .header p {{
                    margin: 10px 0 0 0;
                    color: #ffffff;
                    font-size: 16px;
                    opacity: 0.95;
                }}
                .content {{
                    padding: 40px 30px;
                }}
                .greeting {{
                    font-size: 16px;
                    color: #333333;
                    margin-bottom: 15px;
                }}
                .message {{
                    font-size: 15px;
                    color: #555555;
                    line-height: 1.6;
                    margin-bottom: 20px;
                }}
                .otp-section {{
                    background-color: #fff5f5;
                    border: 2px dashed #ff6b6b;
                    border-radius: 8px;
                    padding: 30px;
                    text-align: center;
                    margin: 30px 0;
                }}
                .otp-label {{
                    font-size: 14px;
                    color: #666666;
                    margin-bottom: 10px;
                }}
                .otp-code {{
                    font-size: 36px;
                    font-weight: 700;
                    color: #ff6b6b;
                    letter-spacing: 8px;
                    font-family: 'Courier New', monospace;
                    margin: 10px 0;
                }}
                .otp-instruction {{
                    font-size: 13px;
                    color: #666666;
                    margin-top: 10px;
                }}
                .warning-box {{
                    background-color: #fff3cd;
                    border-left: 4px solid #ffc107;
                    padding: 15px;
                    margin: 20px 0;
                    border-radius: 4px;
                }}
                .warning-box p {{
                    margin: 0;
                    font-size: 13px;
                    color: #856404;
                }}
                .security-alert {{
                    background-color: #f8d7da;
                    border-left: 4px solid #dc3545;
                    padding: 15px;
                    margin: 20px 0;
                    border-radius: 4px;
                }}
                .security-alert p {{
                    margin: 0;
                    font-size: 13px;
                    color: #721c24;
                }}
                .footer {{
                    text-align: center;
                    padding: 30px;
                    background-color: #f8f9fa;
                    border-top: 1px solid #e9ecef;
                }}
                .footer-text {{
                    font-size: 13px;
                    color: #6c757d;
                    margin: 5px 0;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <h1>🔐 Password Reset Request</h1>
                    <p>We received a request to reset your password</p>
                </div>
                
                <div class="content">
                    <p class="greeting">{greeting}</p>
                    
                    <p class="message">
                        We received a request to reset your password for your YogKulam account.
                    </p>
                    
                    <p class="message">
                        Use the code below to proceed with resetting your password:
                    </p>
                    
                    <div class="otp-section">
                        <div class="otp-label">Your Password Reset Code</div>
                        <div class="otp-code">{otp}</div>
                        <div class="otp-instruction">Enter this code to reset your password</div>
                    </div>
                    
                    <div class="warning-box">
                        <p><strong>⏰ Important:</strong> This code will expire in <strong>10 minutes</strong>.</p>
                    </div>
                    
                    <div class="security-alert">
                        <p><strong>🛡️ Security Alert:</strong> If you didn't request a password reset, please ignore this email and consider changing your password immediately for security reasons.</p>
                    </div>
                </div>
                
                <div class="footer">
                    <p class="footer-text"><strong>Namaste,</strong></p>
                    <p class="footer-text">The YogKulam Team</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        text_content = f"""
        {greeting}
        
        We received a request to reset your password for your YogKulam account.
        
        Your password reset code is: {otp}
        
        This code will expire in 10 minutes.
        
        If you didn't request a password reset, please ignore this email.
        
        Namaste,
        The YogKulam Team
        """
        
        return self.send_email(to_email, subject, html_content, text_content)
    
    def send_welcome_email(self, to_email: str, user_name: str) -> bool:
        """Send welcome email after successful verification - YogKulam Style"""
        
        first_name = user_name.split()[0] if user_name else 'Yogi'
        
        subject = "Welcome to YogKulam - Your Journey Begins!"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    background-color: #f5f5f5;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #ffffff;
                }}
                .header {{
                    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                    padding: 50px 30px;
                    text-align: center;
                }}
                .header h1 {{
                    margin: 0;
                    color: #ffffff;
                    font-size: 32px;
                    font-weight: 600;
                }}
                .header p {{
                    margin: 15px 0 0 0;
                    color: #ffffff;
                    font-size: 18px;
                    opacity: 0.95;
                }}
                .content {{
                    padding: 40px 30px;
                }}
                .greeting {{
                    font-size: 18px;
                    color: #333333;
                    margin-bottom: 20px;
                    font-weight: 500;
                }}
                .message {{
                    font-size: 15px;
                    color: #555555;
                    line-height: 1.7;
                    margin-bottom: 20px;
                }}
                .success-box {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: #ffffff;
                    padding: 30px;
                    border-radius: 12px;
                    text-align: center;
                    margin: 30px 0;
                }}
                .success-icon {{
                    font-size: 48px;
                    margin-bottom: 15px;
                }}
                .success-text {{
                    font-size: 18px;
                    font-weight: 600;
                    margin: 0;
                }}
                .next-steps {{
                    margin: 30px 0;
                }}
                .step-item {{
                    display: flex;
                    align-items: flex-start;
                    margin: 20px 0;
                    padding: 15px;
                    background-color: #f8f9fa;
                    border-radius: 8px;
                }}
                .step-number {{
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: #ffffff;
                    width: 30px;
                    height: 30px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-weight: 700;
                    margin-right: 15px;
                    flex-shrink: 0;
                }}
                .step-content {{
                    flex: 1;
                }}
                .step-title {{
                    font-size: 15px;
                    font-weight: 600;
                    color: #333333;
                    margin: 0 0 5px 0;
                }}
                .step-description {{
                    font-size: 14px;
                    color: #666666;
                    margin: 0;
                }}
                .footer {{
                    text-align: center;
                    padding: 30px;
                    background-color: #f8f9fa;
                    border-top: 1px solid #e9ecef;
                }}
                .footer-text {{
                    font-size: 13px;
                    color: #6c757d;
                    margin: 5px 0;
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <h1>🎉 Welcome to YogKulam!</h1>
                    <p>Your journey to wellness begins now</p>
                </div>
                
                <div class="content">
                    <p class="greeting">Namaste {first_name},</p>
                    
                    <div class="success-box">
                        <div class="success-icon">✨</div>
                        <p class="success-text">Your email has been verified successfully!</p>
                    </div>
                    
                    <p class="message">
                        Congratulations! You're now part of the YogKulam community. We're thrilled to support you on your yoga journey.
                    </p>
                    
                    <p class="message">
                        Here's what you can do next:
                    </p>
                    
                    <div class="next-steps">
                        <div class="step-item">
                            <div class="step-number">1</div>
                            <div class="step-content">
                                <p class="step-title">🧘 Explore Guided Sessions</p>
                                <p class="step-description">Browse our library of yoga sessions for all levels</p>
                            </div>
                        </div>
                        
                        <div class="step-item">
                            <div class="step-number">2</div>
                            <div class="step-content">
                                <p class="step-title">📅 Schedule Your Practice</p>
                                <p class="step-description">Set up your personalized practice schedule</p>
                            </div>
                        </div>
                        
                        <div class="step-item">
                            <div class="step-number">3</div>
                            <div class="step-content">
                                <p class="step-title">👥 Join the Community</p>
                                <p class="step-description">Connect with fellow yogis and share your journey</p>
                            </div>
                        </div>
                        
                        <div class="step-item">
                            <div class="step-number">4</div>
                            <div class="step-content">
                                <p class="step-title">📊 Track Your Progress</p>
                                <p class="step-description">Monitor your achievements and set new goals</p>
                            </div>
                        </div>
                    </div>
                    
                    <p class="message">
                        If you have any questions or need assistance, our support team is always here to help.
                    </p>
                    
                    <p class="message">
                        Let's begin this beautiful journey together! 🙏
                    </p>
                </div>
                
                <div class="footer">
                    <p class="footer-text"><strong>Namaste,</strong></p>
                    <p class="footer-text">The YogKulam Team</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        text_content = f"""
        Namaste {first_name},
        
        Congratulations! Your email has been verified successfully!
        
        You're now part of the YogKulam community. Here's what you can do next:
        
        1. Explore guided yoga sessions
        2. Schedule your practice sessions
        3. Connect with our yoga community
        4. Track your progress and achievements
        
        If you have any questions, our support team is here to help.
        
        Namaste,
        The YogKulam Team
        """
        
        return self.send_email(to_email, subject, html_content, text_content)

# Create singleton instance
email_service = EmailService()
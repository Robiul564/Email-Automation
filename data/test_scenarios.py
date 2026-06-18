"""
Test Data: 10 Unique Email Scenarios
Includes Intent, Key Facts, Tone, and Reference Emails
"""

TEST_SCENARIOS = [
    {
        "scenario_id": 1,
        "intent": "Follow up after initial meeting",
        "key_facts": [
            "Discussed project timeline of 6 months",
            "Budget approved at $50,000",
            "Next milestone is design phase starting next Monday"
        ],
        "tone": "professional and optimistic",
        "reference_email": """Dear Sarah,

Thank you for taking the time to meet with me yesterday. I genuinely appreciated our discussion about the project direction and your insights into the team's expectations.

As we confirmed during our meeting, the project timeline has been set for 6 months with an approved budget of $50,000. I wanted to formally confirm that our next milestone—the design phase—is scheduled to begin next Monday as discussed.

I am genuinely enthusiastic about moving forward and confident that this project will deliver excellent results for your organization. Should you need any additional information or have any clarifying questions, please don't hesitate to reach out.

Best regards,
John Smith"""
    },
    {
        "scenario_id": 2,
        "intent": "Request for proposal details and clarification",
        "key_facts": [
            "Proposal submitted 2 weeks ago",
            "Awaiting client feedback",
            "Decision needed by end of month"
        ],
        "tone": "casual yet professional",
        "reference_email": """Hi Alex,

Hope you're doing well! I wanted to touch base about the proposal I sent over two weeks ago.

I completely understand these things take time to review, but I wanted to make sure everything is clear. Is there anything from the proposal you'd like us to clarify or dive deeper into? Also, just to confirm timeline-wise, we're looking to have your feedback by month-end so we can move things forward smoothly.

Let me know if you have any questions or need anything from our end!

Cheers,
Mike Johnson"""
    },
    {
        "scenario_id": 3,
        "intent": "Urgent request for immediate action",
        "key_facts": [
            "Critical bug discovered in production",
            "Affects 5% of active users",
            "Requires immediate hotfix deployment"
        ],
        "tone": "urgent and direct",
        "reference_email": """To: DevOps Team

URGENT: Critical Bug Fix Required

We have identified a critical bug in production that is impacting approximately 5% of our active users. This issue requires immediate attention and a hotfix deployment as soon as possible.

Please prioritize this task above all other commitments. The bug is affecting core functionality and is impacting user experience significantly. We need this resolved within the next 2 hours if possible.

I will be standing by for updates. Please confirm receipt and estimated deployment time immediately.

Thank you for your immediate attention to this matter.

[Your Name]"""
    },
    {
        "scenario_id": 4,
        "intent": "Express empathy and provide support",
        "key_facts": [
            "Aware of recent project setback",
            "Team faced unexpected technical challenges",
            "Ready to provide additional resources and support"
        ],
        "tone": "empathetic and supportive",
        "reference_email": """Dear Team,

I wanted to reach out personally to express my understanding regarding the recent project setback. I know that encountering unexpected technical challenges can be frustrating and discouraging, especially when the team has been working so diligently.

Please know that I recognize the effort and dedication you've all shown throughout this process. These kinds of obstacles are not a reflection of the team's competence—they're simply part of the development journey. We've all been there.

I want you to know that I'm here to support you in overcoming this challenge. I'm ready to provide any additional resources, expertise, or support that you need to move forward. Please don't hesitate to reach out if there's anything I can do.

We will get through this together.

With appreciation and support,
[Your Name]"""
    },
    {
        "scenario_id": 5,
        "intent": "Introduce new partnership opportunity",
        "key_facts": [
            "Strategic partnership with Fortune 500 company",
            "Expected to increase market reach by 40%",
            "Partnership announcement scheduled for next month"
        ],
        "tone": "excited and forward-looking",
        "reference_email": """Dear [Recipient],

I'm thrilled to share some exciting news with you! We've just finalized a strategic partnership with a Fortune 500 company, and I wanted you to be among the first to know.

This partnership is set to significantly expand our market reach by an estimated 40%, opening doors to new customer segments and growth opportunities we've been working toward. The collaboration aligns perfectly with our long-term vision and strategic goals.

We have an official partnership announcement scheduled for next month, and I'm genuinely excited to share all the details with you at that time. This is a major milestone for our organization, and your support has been instrumental in making this possible.

Looking forward to an amazing journey ahead!

Warm regards,
[Your Name]"""
    },
    {
        "scenario_id": 6,
        "intent": "Polite rejection of business proposal",
        "key_facts": [
            "Appreciated the vendor's comprehensive proposal",
            "Decided to move forward with different solution",
            "Wishes to maintain professional relationship"
        ],
        "tone": "respectful and diplomatic",
        "reference_email": """Dear [Vendor Name],

Thank you so much for taking the time to prepare such a comprehensive proposal for our organization. Your team clearly put considerable effort into understanding our needs and presenting a well-thought-out solution.

After careful consideration and extensive evaluation, we have decided to move forward with a different vendor solution at this time. This decision was not made lightly and reflects our specific strategic direction rather than any shortcoming on your part.

We genuinely appreciate your professionalism throughout this process and would very much like to maintain our professional relationship. Perhaps there may be opportunities to work together in the future.

Thank you again for your time and effort.

Best regards,
[Your Name]"""
    },
    {
        "scenario_id": 7,
        "intent": "Schedule important meeting and confirm details",
        "key_facts": [
            "Meeting with executive leadership",
            "Scheduled for Thursday at 2 PM",
            "Location: Conference Room A"
        ],
        "tone": "formal and precise",
        "reference_email": """Dear Executive Team,

I hope this email finds you well. I am writing to confirm the details of our important meeting scheduled for Thursday at 2:00 PM in Conference Room A.

During this meeting, we will discuss Q3 strategic initiatives, budget allocation, and key performance metrics. Please come prepared to present updates from your respective departments.

Meeting Details:
- Date: Thursday
- Time: 2:00 PM
- Location: Conference Room A
- Duration: 1 hour
- Attendees: Executive Leadership Team

Please confirm your attendance at your earliest convenience. If you have any conflicts or cannot attend, please notify me immediately so we can reschedule if necessary.

Thank you for your attention to this matter.

Sincerely,
[Your Name]"""
    },
    {
        "scenario_id": 8,
        "intent": "Acknowledge receipt and express gratitude",
        "key_facts": [
            "Received donation of $25,000 from supporter",
            "Will directly impact community outreach programs",
            "Donor's generosity is greatly appreciated"
        ],
        "tone": "warm and grateful",
        "reference_email": """Dear [Donor Name],

I am writing to personally express my heartfelt gratitude for your incredibly generous donation of $25,000. Your support means the world to us and will have a tremendous impact on our community outreach programs.

Thanks to donors like you, we are able to continue our mission of making a real difference in people's lives. Your contribution will directly support our education initiatives, helping us reach underserved communities and provide resources where they are needed most.

Your generosity does not go unnoticed, and we are truly grateful for your belief in our mission. We would love to keep you updated on how your donation makes a difference, and we would welcome the opportunity to thank you in person at one of our upcoming events.

With sincere appreciation,
[Your Name]"""
    },
    {
        "scenario_id": 9,
        "intent": "Provide constructive feedback on performance",
        "key_facts": [
            "Overall performance has been solid",
            "Needs improvement in deadline management",
            "Strong technical skills that should be leveraged more"
        ],
        "tone": "constructive and encouraging",
        "reference_email": """Dear [Employee Name],

I wanted to take some time to discuss your performance this quarter. Overall, I'm pleased with your contributions and the solid work you've been delivering.

I've noticed that you have strong technical skills that are truly an asset to the team, and I'd like to see you leverage these strengths even more in your upcoming projects. However, I did want to address an area where we can focus on improvement: deadline management.

I've observed a pattern of projects running slightly over their scheduled timelines. I believe with some focus on planning and time management strategies, this is absolutely something we can address together. I'm here to support you with any resources or mentoring you might need.

Let's schedule a time to discuss strategies for improvement and how I can best support your success.

Best regards,
[Your Name]"""
    },
    {
        "scenario_id": 10,
        "intent": "Announce company-wide organizational changes",
        "key_facts": [
            "New Chief Operating Officer joining next month",
            "Department reorganization to streamline operations",
            "All employees will receive individual briefings"
        ],
        "tone": "informative and reassuring",
        "reference_email": """Dear All,

I am writing to share some important organizational announcements that will take effect next month.

First, I'm excited to announce that we will be welcoming a new Chief Operating Officer to our leadership team. This addition reflects our commitment to strengthening operations and positioning ourselves for sustainable growth.

Additionally, we will be implementing a department reorganization designed to streamline our operations and improve collaboration across teams. These changes have been carefully planned to enhance efficiency while maintaining our strong company culture.

I understand that organizational changes can raise questions and concerns. To address this, all employees will receive individual briefings from their department heads over the coming weeks. These sessions will provide an opportunity to ask questions and discuss how these changes may impact your role.

We are committed to ensuring a smooth transition, and I appreciate your flexibility and continued dedication during this period of growth.

Best regards,
[CEO Name]"""
    }
]


def get_test_scenarios():
    """Returns all test scenarios."""
    return TEST_SCENARIOS


def get_scenario_by_id(scenario_id):
    """Get a specific scenario by ID."""
    for scenario in TEST_SCENARIOS:
        if scenario["scenario_id"] == scenario_id:
            return scenario
    return None

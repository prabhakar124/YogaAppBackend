import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models.blog import Blog, Base
from datetime import datetime, timedelta
import random

# Create tables
Base.metadata.create_all(bind=engine)

# Extended sample blog data (21 total blogs)
SAMPLE_BLOGS = [
    # BLOG 1 - Asanas
    {
        "title": "Master Guide to Surya Namaskar: Transform Your Morning Routine",
        "excerpt": "Discover the ancient art of Sun Salutation and how this powerful sequence can revolutionize your daily practice. Learn proper alignment, breathing techniques, and common mistakes to avoid.",
        "category": "Asanas",
        "category_color": "#ff6b35",
        "author": "Priya Sharma",
        "read_time": "8 min read",
        "image": "https://images.unsplash.com/photo-1588286840104-8957b019727f?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Introduction to Surya Namaskar",
            "12 Poses Explained Step-by-Step",
            "Breathing Techniques & Mantras",
            "Health Benefits & Precautions",
            "Common Mistakes to Avoid",
        ],
        "content": [
            {
                "heading": "Introduction to Surya Namaskar",
                "text": "Surya Namaskar, or Sun Salutation, is one of the most powerful and complete yoga sequences ever developed. This ancient practice combines 12 graceful poses in a flowing sequence that honors the sun, the source of all life on Earth. Dating back thousands of years, this sacred ritual has been practiced by yogis to awaken the body, calm the mind, and energize the spirit.\n\nWhether you're a complete beginner or an experienced practitioner, Surya Namaskar offers countless benefits. It stretches and strengthens every major muscle group, improves cardiovascular health, enhances flexibility, and creates a meditative state of flow. In just 10-15 minutes, you can experience a complete workout that leaves you feeling refreshed and centered.",
                "image": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&h=600&fit=crop",
                "imageAlt": "Person performing Surya Namaskar yoga pose"
            },
            {
                "heading": "12 Poses Explained Step-by-Step",
                "text": "Each of the 12 positions in Surya Namaskar serves a specific purpose. We begin in Pranamasana (Prayer Pose), establishing our intention and connecting with our breath. From there, we flow through Hasta Uttanasana (Raised Arms Pose), Hasta Padasana (Hand to Foot Pose), and continue through the sequence, creating a beautiful symphony of movement and breath.\n\nThe key to mastering Surya Namaskar lies in synchronizing each movement with your breath. Inhale as you extend and open your body, exhale as you fold and contract. This conscious breathing transforms the practice from mere exercise into a moving meditation that calms the nervous system and brings clarity to the mind."
            },
            {
                "heading": "Breathing Techniques & Mantras",
                "text": "In traditional practice, each position of Surya Namaskar is accompanied by a specific mantra that honors the sun's different qualities. These 12 mantras, when chanted with devotion, add a powerful spiritual dimension to the practice. However, even without mantras, maintaining steady, conscious breathing throughout the sequence is essential for maximizing benefits.",
                "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=800&h=600&fit=crop",
                "imageAlt": "Meditation and breathing practice"
            },
            {
                "heading": "Health Benefits & Precautions",
                "text": "Regular practice of Surya Namaskar offers remarkable health benefits including improved digestion, better sleep quality, increased energy levels, weight management, and enhanced mental clarity. It strengthens the immune system, improves posture, and helps regulate hormonal balance.\n\nHowever, it's important to practice safely. Those with high blood pressure, heart conditions, or back problems should consult a qualified yoga teacher before beginning. Pregnant women should modify the practice appropriately, and everyone should listen to their body and respect their current limitations.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Yoga practitioner in meditation pose"
            },
            {
                "heading": "Common Mistakes to Avoid",
                "text": "Many practitioners rush through the sequence, losing the meditative quality and proper alignment. Take your time with each pose, ensuring your foundation is stable before moving to the next position. Another common mistake is holding the breath or breathing shallowly. Remember, the breath is the bridge between body and mind—keep it flowing smoothly throughout your practice.\n\nWith consistent practice, patience, and proper guidance, Surya Namaskar can truly transform your yoga practice and your life. Start with just a few rounds each morning and gradually build up as your strength and flexibility increase."
            }
        ],
        "days_ago": 5
    },
    
    # BLOG 2 - Pranayam
    {
        "title": "Pranayama for Stress Relief: Breathe Your Way to Calm",
        "excerpt": "In today's fast-paced world, stress has become a constant companion. Learn powerful breathing techniques that can instantly calm your nervous system and restore inner peace.",
        "category": "Pranayam",
        "category_color": "#4ecdc4",
        "author": "Amit Kumar",
        "read_time": "6 min read",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Understanding the Stress Response",
            "Nadi Shodhana (Alternate Nostril Breathing)",
            "Bhramari (Bee Breath) Technique",
            "4-7-8 Breathing Method",
            "Creating Your Daily Practice"
        ],
        "content": [
            {
                "heading": "Understanding the Stress Response",
                "text": "In today's fast-paced world, stress has become a constant companion for many of us. When we encounter stressful situations, our body activates the sympathetic nervous system, triggering the fight-or-flight response. This leads to increased heart rate, shallow breathing, and elevated cortisol levels.\n\nPranayama, the ancient yogic practice of breath control, offers a powerful antidote to stress. By consciously regulating our breath, we can activate the parasympathetic nervous system, which promotes relaxation and healing."
            },
            {
                "heading": "Nadi Shodhana (Alternate Nostril Breathing)",
                "text": "Nadi Shodhana is one of the most effective pranayama techniques for calming the mind and balancing the nervous system. This practice involves alternately breathing through each nostril, which helps balance the left and right hemispheres of the brain.\n\nTo practice: Sit comfortably with your spine straight. Use your right thumb to close your right nostril and inhale through the left nostril for a count of 4. Close both nostrils briefly, then release the right nostril and exhale for a count of 4.",
                "image": "https://images.unsplash.com/photo-1593811167562-9cef47bfc4d7?w=800&h=600&fit=crop",
                "imageAlt": "Alternate nostril breathing demonstration"
            },
            {
                "heading": "Bhramari (Bee Breath) Technique",
                "text": "Bhramari pranayama, named after the black Indian bee, is particularly effective for relieving mental tension and anxiety. The humming sound created during this practice creates vibrations that calm the mind and nervous system."
            },
            {
                "heading": "4-7-8 Breathing Method",
                "text": "The 4-7-8 breathing technique, popularized by Dr. Andrew Weil, is a simple yet powerful method for quickly reducing stress and promoting sleep. This practice helps slow down the breath and activate the relaxation response.",
                "image": "https://images.unsplash.com/photo-1447452001602-7090c7ab2db3?w=800&h=600&fit=crop",
                "imageAlt": "Peaceful breathing meditation"
            },
            {
                "heading": "Creating Your Daily Practice",
                "text": "The key to experiencing the full benefits of pranayama is consistency. Start with just 5-10 minutes daily, preferably in the morning on an empty stomach. Choose one or two techniques that resonate with you and practice them regularly."
            }
        ],
        "days_ago": 10
    },
    
    # BLOG 3 - Disease Cure
    {
        "title": "Yoga Therapy for Lower Back Pain: A Comprehensive Healing Guide",
        "excerpt": "Lower back pain affects millions worldwide. Explore evidence-based yoga sequences specifically designed to strengthen, stretch, and heal your back naturally without medication.",
        "category": "Disease Cure",
        "category_color": "#95e1d3",
        "author": "Dr. Meera Patel",
        "read_time": "10 min read",
        "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Understanding Lower Back Pain",
            "Gentle Therapeutic Sequences",
            "Core Strengthening Poses",
            "Props & Modifications",
            "Prevention Strategies",
            "When to See a Doctor"
        ],
        "content": [
            {
                "heading": "Understanding Lower Back Pain",
                "text": "Lower back pain is one of the most common health complaints worldwide, affecting approximately 80% of adults at some point in their lives. The lower back, or lumbar region, bears much of the body's weight and is involved in almost every movement we make.\n\nYoga therapy offers a holistic approach to healing lower back pain by addressing both the physical and mental aspects of the condition. Through gentle stretching, strengthening, and mindful movement, yoga can help alleviate pain, improve flexibility, and prevent future injuries.",
                "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=800&h=600&fit=crop",
                "imageAlt": "Yoga therapy for back pain"
            },
            {
                "heading": "Gentle Therapeutic Sequences",
                "text": "When dealing with lower back pain, it's crucial to start with gentle, therapeutic movements that don't strain the injured area. Begin with Cat-Cow poses to gently warm up the spine. Move slowly between arching and rounding your back, synchronizing movement with breath."
            },
            {
                "heading": "Core Strengthening Poses",
                "text": "A strong core is essential for supporting the lower back and preventing future pain. However, it's important to strengthen the core without straining the back. Bridge Pose is excellent for this purpose.",
                "image": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&h=600&fit=crop",
                "imageAlt": "Core strengthening yoga pose"
            },
            {
                "heading": "Props & Modifications",
                "text": "Using props can make yoga therapy more accessible and effective for lower back pain. Yoga blocks can help you maintain proper alignment in standing forward folds without straining your back."
            },
            {
                "heading": "Prevention Strategies",
                "text": "Preventing lower back pain is far easier than treating it. Maintain good posture throughout the day, whether sitting or standing. When sitting for long periods, use lumbar support and take regular breaks to stand and stretch.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Proper posture and alignment"
            },
            {
                "heading": "When to See a Doctor",
                "text": "While yoga therapy can be highly effective for many types of lower back pain, it's important to know when to seek medical attention. Consult a doctor if your pain is severe, persists for more than a few weeks, or is accompanied by numbness, tingling, or weakness in the legs."
            }
        ],
        "days_ago": 15
    },
    
    # BLOG 4 - Meditation
    {
        "title": "Mindfulness Meditation: The Complete Beginner's Journey",
        "excerpt": "Start your meditation journey with confidence. This comprehensive guide covers everything from finding your perfect posture to dealing with a wandering mind and building a sustainable practice.",
        "category": "Meditation",
        "category_color": "#a8e6cf",
        "author": "Raj Desai",
        "read_time": "12 min read",
        "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "What is Mindfulness Meditation?",
            "Setting Up Your Space",
            "Basic Techniques for Beginners",
            "Dealing with Common Challenges",
            "Building a Daily Habit",
            "Advanced Practices"
        ],
        "content": [
            {
                "heading": "What is Mindfulness Meditation?",
                "text": "Mindfulness meditation is the practice of bringing one's complete attention to the present moment without judgment. Rooted in Buddhist traditions but now widely practiced in secular contexts, mindfulness has been scientifically proven to reduce stress, improve focus, enhance emotional regulation, and promote overall well-being.",
                "image": "https://images.unsplash.com/photo-1499209974431-9dddcece7f88?w=800&h=600&fit=crop",
                "imageAlt": "Peaceful meditation setting"
            },
            {
                "heading": "Setting Up Your Space",
                "text": "Creating a dedicated meditation space can significantly enhance your practice. Choose a quiet corner of your home where you're unlikely to be disturbed. The space doesn't need to be large—even a small cushion in a corner will work."
            },
            {
                "heading": "Basic Techniques for Beginners",
                "text": "Start with breath awareness meditation, the foundation of mindfulness practice. Sit comfortably with your eyes closed or softly gazing downward. Bring your attention to your natural breath, noticing the sensation of air moving in and out of your nostrils or the rise and fall of your belly.",
                "image": "https://images.unsplash.com/photo-1593811167562-9cef47bfc4d7?w=800&h=600&fit=crop",
                "imageAlt": "Meditation breathing technique"
            },
            {
                "heading": "Dealing with Common Challenges",
                "text": "Every meditator faces challenges. The wandering mind is not a problem—it's expected. Research shows the average person has thousands of thoughts per day. Don't judge yourself for thinking; simply notice and return to your anchor."
            },
            {
                "heading": "Building a Daily Habit",
                "text": "Consistency is more important than duration. It's better to meditate for 5 minutes every day than 30 minutes once a week. Choose a specific time and place for your practice to establish a routine.",
                "image": "https://images.unsplash.com/photo-1447452001602-7090c7ab2db3?w=800&h=600&fit=crop",
                "imageAlt": "Daily meditation practice"
            },
            {
                "heading": "Advanced Practices",
                "text": "Once you're comfortable with basic breath awareness, you can explore other mindfulness practices. Loving-kindness meditation cultivates compassion toward yourself and others. Start by directing kind wishes toward yourself, then gradually extend them to loved ones, acquaintances, and even difficult people."
            }
        ],
        "days_ago": 20
    },
    
    # BLOG 5 - Philosophy
    {
        "title": "The Eight Limbs of Yoga: Ancient Wisdom for Modern Living",
        "excerpt": "Dive deep into Patanjali's Yoga Sutras and discover how the eight limbs of yoga provide a complete framework for living a meaningful, balanced, and enlightened life in today's world.",
        "category": "Philosophy",
        "category_color": "#ffd93d",
        "author": "Swami Ananda",
        "read_time": "15 min read",
        "image": "https://images.unsplash.com/photo-1499209974431-9dddcece7f88?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Introduction to Ashtanga Yoga",
            "Yama: Ethical Standards",
            "Niyama: Self-Discipline",
            "Asana: Physical Postures",
            "Pranayama: Breath Control",
            "Pratyahara to Samadhi",
            "Practical Applications Today"
        ],
        "content": [
            {
                "heading": "Introduction to Ashtanga Yoga",
                "text": "The Eight Limbs of Yoga, or Ashtanga Yoga, were codified by the sage Patanjali in the Yoga Sutras over 2,000 years ago. This comprehensive system provides a philosophical and practical framework for living a meaningful, purposeful life."
            },
            {
                "heading": "Yama: Ethical Standards",
                "text": "The Yamas are five ethical guidelines that govern our interactions with others and the world around us. These form the foundation of yogic philosophy and are remarkably relevant to modern life.\n\nAhimsa (non-violence) is the first and most important Yama. It extends beyond physical violence to include harmful thoughts, words, and actions.",
                "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=800&h=600&fit=crop",
                "imageAlt": "Yoga philosophy and ethics"
            },
            {
                "heading": "Niyama: Self-Discipline",
                "text": "The Niyamas are five personal observances that guide our relationship with ourselves. These practices help us develop the inner discipline necessary for spiritual growth."
            },
            {
                "heading": "Asana: Physical Postures",
                "text": "Asana, the third limb, is what most people think of as yoga. However, in Patanjali's original text, asana simply meant a comfortable, stable seat for meditation. The physical postures we practice today developed later as a way to prepare the body for meditation.",
                "image": "https://images.unsplash.com/photo-1588286840104-8957b019727f?w=800&h=600&fit=crop",
                "imageAlt": "Yoga asana practice"
            },
            {
                "heading": "Pranayama: Breath Control",
                "text": "Pranayama, the fourth limb, is the practice of breath control. In Sanskrit, 'prana' means life force or vital energy, and 'ayama' means to extend or draw out. Through pranayama, we learn to harness and direct our life force energy."
            },
            {
                "heading": "Pratyahara to Samadhi",
                "text": "Pratyahara (withdrawal of senses) is the bridge between the external practices and the internal practices. It involves consciously withdrawing attention from external stimuli and turning it inward.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Deep meditation and samadhi"
            },
            {
                "heading": "Practical Applications Today",
                "text": "The Eight Limbs of Yoga offer timeless wisdom for modern challenges. In our fast-paced, technology-driven world, these ancient teachings are more relevant than ever."
            }
        ],
        "days_ago": 25
    },
    
    # BLOG 6 - YTT
    {
        "title": "How to Choose the Right Yoga Teacher Training Program",
        "excerpt": "Selecting a YTT program is a significant decision. Learn the key factors to consider, questions to ask, and red flags to watch for when choosing your yoga teacher training.",
        "category": "YTT",
        "category_color": "#6c5ce7",
        "author": "Kavita Singh",
        "read_time": "9 min read",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Understanding YTT Certifications",
            "In-Person vs Online Training",
            "Evaluating Program Curriculum",
            "Checking Instructor Credentials",
            "Cost and Investment Considerations",
            "Making Your Final Decision"
        ],
        "content": [
            {
                "heading": "Understanding YTT Certifications",
                "text": "Yoga Teacher Training (YTT) programs come in various levels, with 200-hour, 300-hour, and 500-hour certifications being the most common. The 200-hour YTT is the foundational certification that qualifies you to teach yoga in most studios and gyms.",
                "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&h=600&fit=crop",
                "imageAlt": "Yoga teacher training session"
            },
            {
                "heading": "In-Person vs Online Training",
                "text": "The COVID-19 pandemic accelerated the acceptance of online yoga teacher training, and now many reputable programs offer hybrid or fully online options. Each format has distinct advantages and considerations."
            },
            {
                "heading": "Evaluating Program Curriculum",
                "text": "A comprehensive YTT curriculum should cover five main areas: techniques, teaching methodology, anatomy and physiology, yoga philosophy and lifestyle, and practicum.",
                "image": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&h=600&fit=crop",
                "imageAlt": "YTT curriculum study materials"
            },
            {
                "heading": "Checking Instructor Credentials",
                "text": "The quality of your teacher training largely depends on your instructors. Research the lead teacher's background thoroughly. How long have they been teaching? What is their training background?"
            },
            {
                "heading": "Cost and Investment Considerations",
                "text": "YTT programs vary widely in cost, typically ranging from $2,000 to $5,000 for a 200-hour certification, though some luxury retreat-style programs can cost significantly more.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Investment in yoga teacher training"
            },
            {
                "heading": "Making Your Final Decision",
                "text": "After researching options, narrow your choices to 2-3 programs. If possible, attend an open house, sample class, or information session. This gives you a feel for the space, instructors, and program culture."
            }
        ],
        "days_ago": 30
    },

    # BLOG 7 - Asanas
    {
        "title": "Warrior Poses Mastery: Build Strength and Confidence",
        "excerpt": "The warrior series (Virabhadrasana I, II, and III) are foundational standing poses that build strength, stamina, and mental focus. Learn how to master these powerful asanas.",
        "category": "Asanas",
        "category_color": "#ff6b35",
        "author": "Vikram Mehta",
        "read_time": "7 min read",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "The Warrior Lineage in Yoga",
            "Warrior I: Foundation and Power",
            "Warrior II: Stability and Grace",
            "Warrior III: Balance and Focus",
            "Modifications for All Levels"
        ],
        "content": [
            {
                "heading": "The Warrior Lineage in Yoga",
                "text": "The warrior poses are named after Virabhadra, a fierce warrior incarnation of Lord Shiva. These poses embody the qualities of a spiritual warrior: strength, courage, and determination balanced with grace and mindfulness.\n\nPracticing warrior poses regularly builds both physical and mental resilience, teaching us to stand firm in the face of life's challenges while maintaining inner peace.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Warrior pose demonstration"
            },
            {
                "heading": "Warrior I: Foundation and Power",
                "text": "Warrior I (Virabhadrasana I) is a powerful standing pose that opens the hips, chest, and shoulders while strengthening the legs and core. Begin with feet hip-width apart, step one foot back about 3-4 feet, keeping the back foot at a 45-degree angle.\n\nBend the front knee to 90 degrees, ensuring it stays aligned over the ankle. Raise arms overhead, palms facing each other, and gaze forward or slightly up. Hold for 5-10 breaths, feeling your connection to the earth while reaching toward the sky."
            },
            {
                "heading": "Warrior II: Stability and Grace",
                "text": "Warrior II builds upon the foundation of Warrior I, emphasizing hip opening and lateral strength. From a wide stance, turn your front foot out 90 degrees and back foot in slightly. Extend arms parallel to the floor, gazing over the front fingertips.\n\nThis pose cultivates steadiness and determination. Keep your torso upright, shoulders relaxed, and weight evenly distributed between both feet. Breathe deeply, embodying the warrior's focused yet peaceful state.",
                "image": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&h=600&fit=crop",
                "imageAlt": "Warrior II yoga pose"
            },
            {
                "heading": "Warrior III: Balance and Focus",
                "text": "Warrior III is a challenging balancing pose that requires full-body engagement and mental concentration. From Warrior I, shift weight onto the front leg and extend the back leg parallel to the floor while hinging forward at the hips.\n\nExtend arms forward or alongside the body, creating one straight line from fingertips to back toes. This pose develops balance, core strength, and the ability to maintain focus amid challenge."
            },
            {
                "heading": "Modifications for All Levels",
                "text": "Beginners can practice warrior poses with a shorter stance and less depth in the knee bend. Use a wall for support in Warrior III, or keep the back toes on the ground. Advanced practitioners can deepen the poses, hold them longer, or transition dynamically between variations.\n\nRemember, the true warrior spirit is not about achieving the perfect pose, but about showing up with courage and dedication to your practice, honoring where you are today."
            }
        ],
        "days_ago": 3
    },

    # BLOG 8 - Pranayam
    {
        "title": "Kapalabhati: The Skull-Shining Breath for Energy and Clarity",
        "excerpt": "Learn Kapalabhati, a powerful cleansing breath that energizes the body, clears the mind, and detoxifies the respiratory system. Perfect for morning practice.",
        "category": "Pranayam",
        "category_color": "#4ecdc4",
        "author": "Ananya Reddy",
        "read_time": "5 min read",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "What is Kapalabhati?",
            "Technique and Practice",
            "Benefits for Body and Mind",
            "Precautions and Contraindications",
            "Integrating into Your Routine"
        ],
        "content": [
            {
                "heading": "What is Kapalabhati?",
                "text": "Kapalabhati, meaning 'skull-shining breath' in Sanskrit, is a pranayama technique that involves forceful exhalations followed by passive inhalations. This practice is considered one of the six purification techniques (Shatkarmas) in Hatha Yoga.\n\nThe technique generates heat in the body, stimulates the digestive system, and brings clarity to the mind—hence the name 'skull-shining,' as practitioners often experience a sensation of mental brightness after practice.",
                "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=800&h=600&fit=crop",
                "imageAlt": "Kapalabhati breathing practice"
            },
            {
                "heading": "Technique and Practice",
                "text": "Sit in a comfortable meditation position with spine erect. Place hands on knees in chin or jnana mudra. Take a deep breath in, then begin forceful exhalations through the nose, allowing the inhale to happen passively.\n\nThe movement comes from the lower belly, which contracts sharply with each exhale. Start with 20-30 breaths per round, gradually building to 108 or more. Complete 3-5 rounds with brief rest periods between."
            },
            {
                "heading": "Benefits for Body and Mind",
                "text": "Kapalabhati offers numerous benefits: it strengthens abdominal muscles, improves lung capacity, stimulates digestive organs, and enhances concentration. The practice also helps clear nasal passages, energizes the entire system, and is particularly effective for combating morning sluggishness.\n\nRegular practice can improve metabolic rate, support weight management, and create a sense of mental alertness and emotional stability. Many practitioners report feeling more awake and focused after just a few rounds.",
                "image": "https://images.unsplash.com/photo-1593811167562-9cef47bfc4d7?w=800&h=600&fit=crop",
                "imageAlt": "Morning pranayama practice"
            },
            {
                "heading": "Precautions and Contraindications",
                "text": "While powerful, Kapalabhati is not suitable for everyone. Avoid this practice if you're pregnant, have high blood pressure, heart disease, hernia, or recent abdominal surgery. Those with respiratory issues should consult a doctor before beginning.\n\nIf you feel dizzy, lightheaded, or uncomfortable at any point, stop immediately and return to normal breathing. Never force the breath or practice beyond your comfortable capacity."
            },
            {
                "heading": "Integrating into Your Routine",
                "text": "Practice Kapalabhati on an empty stomach, ideally in the morning. Start slowly with just one or two rounds and gradually increase as your capacity improves. Follow with a few minutes of calm, natural breathing to integrate the effects.\n\nThis practice pairs beautifully with other pranayama techniques and meditation, serving as an energizing start to your morning yoga routine or as a midday pick-me-up when energy levels dip."
            }
        ],
        "days_ago": 7
    },

    # BLOG 9 - Disease Cure
    {
        "title": "Yoga for Better Sleep: Natural Solutions for Insomnia",
        "excerpt": "Struggling with sleep? Discover gentle yoga sequences and relaxation techniques that prepare your body and mind for deep, restorative sleep without medication.",
        "category": "Disease Cure",
        "category_color": "#95e1d3",
        "author": "Dr. Sarah Mitchell",
        "read_time": "8 min read",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Understanding Sleep Disorders",
            "Evening Yoga Sequence",
            "Restorative Poses for Relaxation",
            "Breathing Exercises for Sleep",
            "Creating a Bedtime Routine"
        ],
        "content": [
            {
                "heading": "Understanding Sleep Disorders",
                "text": "Insomnia and poor sleep quality affect millions of people worldwide, leading to decreased energy, impaired cognitive function, and various health issues. While there are many causes of sleep problems, stress, anxiety, and physical tension are among the most common.\n\nYoga offers a holistic approach to improving sleep by addressing both the physical and mental aspects of rest. Through gentle movement, conscious breathing, and relaxation techniques, we can signal to our nervous system that it's safe to let go and rest.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Peaceful evening yoga"
            },
            {
                "heading": "Evening Yoga Sequence",
                "text": "Practice this 15-minute sequence 30-60 minutes before bedtime. Begin with gentle neck rolls and shoulder shrugs to release tension. Move into Cat-Cow poses for 5-10 rounds, then transition to Child's Pose for 2-3 minutes.\n\nContinue with Supine Twist (both sides), Happy Baby pose, and Reclining Bound Angle pose. End with Legs-Up-the-Wall pose for 5-10 minutes. Move slowly and mindfully, synchronizing breath with movement."
            },
            {
                "heading": "Restorative Poses for Relaxation",
                "text": "Restorative yoga poses held for longer periods with props allow the body to deeply relax. Supported Child's Pose with a bolster under the torso is especially calming. Supported Bridge Pose with a block under the sacrum gently opens the chest.\n\nThese poses activate the parasympathetic nervous system, lowering heart rate and blood pressure while promoting a sense of safety and calm—essential conditions for good sleep.",
                "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=800&h=600&fit=crop",
                "imageAlt": "Restorative yoga for sleep"
            },
            {
                "heading": "Breathing Exercises for Sleep",
                "text": "The 4-7-8 breath is particularly effective for promoting sleep: inhale for 4 counts, hold for 7, exhale for 8. Repeat 4-8 cycles. This pattern slows the heart rate and activates the relaxation response.\n\nAlternate Nostril Breathing (Nadi Shodhana) performed for 5-10 minutes can also calm an overactive mind. Focus on smooth, even breaths without force or strain."
            },
            {
                "heading": "Creating a Bedtime Routine",
                "text": "Consistency is key for improving sleep. Establish a regular bedtime and stick to it, even on weekends. Create a calming environment: dim lights, cool temperature, minimal screen time an hour before bed.\n\nIncorporate your yoga practice into this routine, along with other relaxing activities like reading, gentle music, or aromatherapy. Over time, these cues will signal to your body that it's time to wind down and prepare for restful sleep."
            }
        ],
        "days_ago": 12
    },

    # BLOG 10 - Meditation
    {
        "title": "Loving-Kindness Meditation: Cultivating Compassion for Self and Others",
        "excerpt": "Metta meditation, or loving-kindness practice, is a powerful technique for developing compassion, reducing negative emotions, and fostering genuine connection with all beings.",
        "category": "Meditation",
        "category_color": "#a8e6cf",
        "author": "Tenzin Norbu",
        "read_time": "10 min read",
        "image": "https://images.unsplash.com/photo-1499209974431-9dddcece7f88?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Origins of Loving-Kindness Meditation",
            "The Four Brahmaviharas",
            "Step-by-Step Practice Guide",
            "Extending Metta to Difficult People",
            "Benefits and Scientific Research"
        ],
        "content": [
            {
                "heading": "Origins of Loving-Kindness Meditation",
                "text": "Loving-kindness meditation, or Metta Bhavana, originates from Buddhist traditions and has been practiced for over 2,500 years. 'Metta' in Pali means loving-kindness, friendliness, or goodwill—a sincere wish for the happiness and well-being of all beings.\n\nThis practice counters the mind's tendency toward judgment, criticism, and negativity by intentionally cultivating feelings of warmth, care, and genuine concern for ourselves and others. It's not about forcing positive feelings but creating conditions for them to arise naturally.",
                "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=800&h=600&fit=crop",
                "imageAlt": "Loving-kindness meditation practice"
            },
            {
                "heading": "The Four Brahmaviharas",
                "text": "Loving-kindness is one of the Four Brahmaviharas (divine abodes) in Buddhist psychology: Metta (loving-kindness), Karuna (compassion for suffering), Mudita (sympathetic joy), and Upekkha (equanimity).\n\nTogether, these qualities form a complete framework for healthy relationships with ourselves and others. Metta is the foundation, the wish for happiness. Karuna responds to suffering with compassion. Mudita celebrates others' joy. Upekkha maintains balance through it all."
            },
            {
                "heading": "Step-by-Step Practice Guide",
                "text": "Begin by sitting comfortably and taking a few deep breaths to settle. Start by directing loving-kindness toward yourself: 'May I be happy. May I be healthy. May I be safe. May I live with ease.' Feel the warmth of these wishes.\n\nNext, bring to mind someone you care about deeply and direct the same phrases toward them. Then extend to a neutral person, someone you neither like nor dislike. Finally, include someone difficult, and ultimately all beings everywhere. Spend 2-5 minutes with each person or group.",
                "image": "https://images.unsplash.com/photo-1447452001602-7090c7ab2db3?w=800&h=600&fit=crop",
                "imageAlt": "Compassion meditation"
            },
            {
                "heading": "Extending Metta to Difficult People",
                "text": "Working with difficult people in Metta practice can be challenging but transformative. Start with someone only mildly difficult, not your worst enemy. Remember, you're not condoning harmful behavior—you're wishing for their happiness because happy people cause less harm.\n\nIf resistance arises, return to self-compassion first. It's okay if you don't feel warm feelings toward difficult people immediately. The practice is in the intention and repetition, not in forcing feelings that aren't genuine."
            },
            {
                "heading": "Benefits and Scientific Research",
                "text": "Research shows that regular loving-kindness meditation increases positive emotions, life satisfaction, and sense of purpose while decreasing symptoms of depression and anxiety. Studies using fMRI scans show increased activity in brain regions associated with empathy and emotional processing.\n\nThe practice has also been shown to reduce implicit bias, increase feelings of social connection, and even improve physical health markers like heart rate variability. Just a few minutes daily can create measurable changes in emotional well-being and interpersonal relationships."
        }
        ],
        "days_ago": 18
    },

    # BLOG 11 - Philosophy
    {
        "title": "The Bhagavad Gita: Timeless Wisdom for Modern Life",
        "excerpt": "Explore the profound teachings of the Bhagavad Gita and discover how this ancient text offers practical guidance for navigating life's challenges, finding purpose, and living with integrity.",
        "category": "Philosophy",
        "category_color": "#ffd93d",
        "author": "Prof. Ramesh Krishnan",
        "read_time": "14 min read",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Introduction to the Gita",
            "The Battlefield as Metaphor",
            "Karma Yoga: The Path of Action",
            "Bhakti Yoga: The Path of Devotion",
            "Jnana Yoga: The Path of Knowledge",
            "Living the Gita's Teachings Today"
        ],
        "content": [
            {
                "heading": "Introduction to the Gita",
                "text": "The Bhagavad Gita, often called simply 'the Gita,' is a 700-verse Hindu scripture that forms part of the epic Mahabharata. Composed between the 5th and 2nd century BCE, it presents a dialogue between Prince Arjuna and his charioteer Krishna, who reveals himself as the Supreme Divine.\n\nDespite its ancient origins, the Gita addresses universal human concerns: duty vs. desire, action vs. inaction, material vs. spiritual life. Its teachings transcend religious boundaries, offering practical wisdom for anyone seeking to live with greater purpose and integrity.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Ancient yoga philosophy"
            },
            {
                "heading": "The Battlefield as Metaphor",
                "text": "The Gita opens on the battlefield of Kurukshetra, where Arjuna faces an ethical dilemma: should he fight in a war against his own relatives, teachers, and friends? Paralyzed by doubt and grief, he seeks guidance from Krishna.\n\nThis battlefield represents the internal conflicts we all face: competing values, difficult choices, and the struggle between our higher and lower natures. The war is really about the inner battle between wisdom and ignorance, light and darkness, selflessness and selfishness."
            },
            {
                "heading": "Karma Yoga: The Path of Action",
                "text": "Krishna teaches that we cannot escape action—even choosing not to act is itself an action. Instead, we must learn to act skillfully, performing our duties without attachment to results. This is Karma Yoga, the path of selfless action.\n\n'You have a right to perform your prescribed duty, but you are not entitled to the fruits of action. Never consider yourself the cause of the results, nor be attached to not doing your duty.' This teaching frees us from anxiety about outcomes while inspiring wholehearted engagement with life.",
                "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=800&h=600&fit=crop",
                "imageAlt": "Karma yoga practice"
            },
            {
                "heading": "Bhakti Yoga: The Path of Devotion",
                "text": "The Gita also emphasizes Bhakti Yoga, the path of loving devotion to the Divine. Krishna reveals that regardless of how we conceive of or name the Divine, sincere devotion leads to spiritual realization.\n\nThis path is accessible to everyone, regardless of intellectual capacity or circumstances. It requires only an open heart and genuine longing for truth. Through devotion, we transform ordinary actions into offerings, making all of life sacred."
            },
            {
                "heading": "Jnana Yoga: The Path of Knowledge",
                "text": "Jnana Yoga, the path of wisdom, involves discriminating between the eternal and temporary, real and unreal. The Gita teaches that our true nature is not the body or even the mind, but the immortal soul (Atman) which is one with the universal consciousness (Brahman).\n\nUnderstanding this fundamental unity removes the illusion of separation that causes suffering. We see the Divine in all beings and act from this awareness of oneness rather than from ego and division."
            },
            {
                "heading": "Living the Gita's Teachings Today",
                "text": "The Gita's wisdom remains profoundly relevant. When facing difficult decisions, we can ask: What is my dharma (duty) in this situation? Can I act without attachment to outcomes? How can I serve something greater than my personal desires?\n\nIn our work, we can practice Karma Yoga by focusing on quality effort rather than rewards. In relationships, Bhakti Yoga teaches us to see the Divine in others. Through study and reflection, Jnana Yoga helps us remember our true nature beyond temporary identities and roles. These paths aren't separate but complementary approaches to living with wisdom, love, and purpose."
            }
        ],
        "days_ago": 22
    },

    # BLOG 12 - YTT
    {
        "title": "Teaching Your First Yoga Class: A Complete Guide",
        "excerpt": "Nervous about teaching your first class after certification? This comprehensive guide covers everything from sequencing and cueing to managing nerves and building confidence as a new teacher.",
        "category": "YTT",
        "category_color": "#6c5ce7",
        "author": "Lisa Thompson, E-RYT 500",
        "read_time": "11 min read",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Preparing Your First Sequence",
            "Effective Cueing Techniques",
            "Creating a Welcoming Environment",
            "Managing Pre-Class Nerves",
            "Learning from Every Class",
            "Building Your Teaching Confidence"
        ],
        "content": [
            {
                "heading": "Preparing Your First Sequence",
                "text": "Your first class doesn't need to be complicated. Start with a straightforward 60-minute sequence that follows a logical arc: warm-up, standing poses, peak pose, cool-down, and savasana. Choose familiar poses you can teach confidently rather than trying to showcase everything you learned in training.\n\nWrite out your sequence with approximate timing for each section. Include options for modifications and variations, but don't over-plan. The best teachers balance structure with flexibility, adapting to their students' needs in the moment.",
                "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&h=600&fit=crop",
                "imageAlt": "Yoga teacher planning class"
            },
            {
                "heading": "Effective Cueing Techniques",
                "text": "Clear, concise cues help students move safely and mindfully. Use anatomical language ('bend your right knee') along with sensory cues ('feel your feet grounding into the earth'). Demonstrate when helpful, but remember that verbal cues develop students' body awareness.\n\nPace your instructions appropriately. Give students time to settle into poses before offering refinements. Watch your class and adjust your cueing based on what you observe rather than sticking rigidly to a script."
            },
            {
                "heading": "Creating a Welcoming Environment",
                "text": "Arrive early to set up the space, test music/equipment, and greet students as they enter. Learn names and ask about injuries or concerns. This personal attention makes students feel valued and helps you teach more responsively.\n\nYour energy sets the tone for the class. Even if you're nervous, bring warmth, presence, and authentic enthusiasm. Students respond to teachers who are genuine, not those trying to project an image of perfection.",
                "image": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&h=600&fit=crop",
                "imageAlt": "Welcoming yoga studio environment"
            },
            {
                "heading": "Managing Pre-Class Nerves",
                "text": "Feeling nervous before your first class is completely normal—it shows you care about doing well. Transform nervous energy into focused attention through breath awareness. Take a few minutes before class for your own centering practice.\n\nRemember, you don't need to be perfect. Students appreciate authentic teachers who are present and caring more than those who appear flawless but disconnected. Your nervousness will decrease dramatically after your first few classes."
            },
            {
                "heading": "Learning from Every Class",
                "text": "After class, take notes while the experience is fresh. What went well? What would you adjust? Did students respond positively to certain cues or sequences? This reflection helps you grow quickly as a teacher.\n\nSeek feedback from trusted students, mentors, or fellow teachers. Record yourself teaching occasionally to identify habits and areas for improvement. Every class is an opportunity to refine your skills."
            },
            {
                "heading": "Building Your Teaching Confidence",
                "text": "Confidence comes from experience, not from knowing everything before you begin. Accept that you'll make mistakes—they're valuable learning opportunities. The key is showing up consistently, staying curious, and maintaining beginner's mind.\n\nContinue your own practice and ongoing education. The best teachers remain students throughout their careers, always deepening their understanding and expanding their skills. Trust that you have valuable gifts to share with your students, even as you continue growing."
            }
        ],
        "days_ago": 28
    },

    # BLOG 13 - Asanas
    {
        "title": "Backbends for Beginners: Opening Your Heart Safely",
        "excerpt": "Backbends can feel intimidating, but when practiced correctly, they're incredibly beneficial for posture, breathing, and emotional well-being. Learn how to approach these poses safely and mindfully.",
        "category": "Asanas",
        "category_color": "#ff6b35",
        "author": "Maya Patel",
        "read_time": "9 min read",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Understanding Backbends",
            "Preparing Your Spine",
            "Gentle Backbends for Beginners",
            "Common Mistakes to Avoid",
            "Building to Deeper Backbends"
        ],
        "content": [
            {
                "heading": "Understanding Backbends",
                "text": "Backbends, or spinal extensions, counteract the forward-bending posture many of us adopt throughout the day—hunching over computers, phones, and desks. These poses open the front body, strengthen the back body, and create space in the chest for fuller breathing.\n\nBackbends also have emotional effects, often described as 'heart-opening.' When we reverse our habitual protective curling inward, we can access feelings of vulnerability, openness, and courage. This makes backbends both physically and emotionally therapeutic.",
                "image": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&h=600&fit=crop",
                "imageAlt": "Gentle backbend demonstration"
            },
            {
                "heading": "Preparing Your Spine",
                "text": "Never jump into deep backbends without proper warm-up. Begin with Cat-Cow poses to gently articulate the spine. Include hip openers like Low Lunge, as tight hip flexors limit backbending range. Shoulder openers are equally important—try Cow Face arms or threading the needle.\n\nStrengthen your back muscles with locust pose variations. A strong back supports safe, sustainable backbending practice without relying solely on flexibility or momentum."
            },
            {
                "heading": "Gentle Backbends for Beginners",
                "text": "Start with Cobra Pose: lie on your belly, hands beside your chest, and lift only as high as comfortable while keeping elbows bent. Focus on lengthening the spine rather than how high you lift.\n\nBridge Pose is another excellent beginner backbend. Lie on your back, feet hip-width apart, and lift your hips. This pose is safer for those with neck issues than deeper backbends like Wheel Pose. Sphinx Pose offers gentle extension with less intensity than Cobra.",
                "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=800&h=600&fit=crop",
                "imageAlt": "Bridge pose for beginners"
            },
            {
                "heading": "Common Mistakes to Avoid",
                "text": "The biggest mistake is compressing the lower back by over-arching. Instead, think about lengthening the spine and distributing the curve evenly. Engage your legs and core to protect your lower back.\n\nAvoid letting your head drop back too far too quickly, which can strain the neck. Keep shoulders away from ears and broaden your collarbones. Never force a backbend—work gradually and respect your body's limits."
            },
            {
                "heading": "Building to Deeper Backbends",
                "text": "Once comfortable with gentle backbends, progress to Camel Pose, keeping hands on your lower back until you're ready to reach for heels. Wheel Pose (Urdhva Dhanurasana) is the culmination of backbending practice, requiring strength, flexibility, and confidence.\n\nApproach Wheel progressively: start with Bridge, then try lifting one leg at a time. When ready for full Wheel, press up from Bridge, ensuring your foundation is strong before fully extending. Always follow backbends with a gentle forward fold or twist to neutralize the spine."
            }
        ],
        "days_ago": 4
    },

    # BLOG 14 - Pranayam
    {
        "title": "Ujjayi Breath: The Victorious Breath for Focus and Calm",
        "excerpt": "Master Ujjayi pranayama, the oceanic breath used throughout vinyasa yoga practice. Learn how this powerful technique builds heat, maintains focus, and creates a meditative state during asana practice.",
        "category": "Pranayam",
        "category_color": "#4ecdc4",
        "author": "Rohan Kapoor",
        "read_time": "6 min read",
        "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "What is Ujjayi Breath?",
            "How to Practice Ujjayi",
            "Benefits During Asana Practice",
            "Common Challenges",
            "Beyond the Mat"
        ],
        "content": [
            {
                "heading": "What is Ujjayi Breath?",
                "text": "Ujjayi pranayama, often called 'victorious breath' or 'ocean breath,' is a breathing technique that creates a soft hissing or ocean-like sound by gently constricting the back of the throat. This audible breath serves as an anchor for attention during yoga practice and life.\n\nThe technique has been used for centuries in yoga traditions, particularly in Ashtanga and Vinyasa styles, where it helps synchronize breath with movement and maintain concentration throughout challenging sequences.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Ujjayi breathing technique"
            },
            {
                "heading": "How to Practice Ujjayi",
                "text": "To learn the sensation, imagine fogging up a mirror with your mouth open. Feel the slight constriction at the back of your throat. Now close your mouth and breathe that same way through your nose, creating a gentle whisper-like sound.\n\nThe sound should be audible to you but not loud or forced. Both inhale and exhale produce the oceanic sound. The breath should feel smooth and even, with no strain. Practice seated first before integrating it into asana practice."
            },
            {
                "heading": "Benefits During Asana Practice",
                "text": "Ujjayi breath regulates breath pace, preventing rushing through sequences. The slight resistance created by the throat constriction lengthens each breath, naturally slowing your practice and increasing oxygen intake.\n\nThis breath generates internal heat (tapas), which warms muscles and increases flexibility. The audible quality keeps your mind focused on the present moment, preventing it from wandering. Many practitioners find Ujjayi breath helps them stay calm in challenging poses.",
                "image": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&h=600&fit=crop",
                "imageAlt": "Vinyasa yoga with Ujjayi breath"
            },
            {
                "heading": "Common Challenges",
                "text": "Beginners often make the breath too loud or forceful, which creates tension rather than ease. The sound should be soft and sustainable for long periods. If you feel strained, return to normal breathing and try again more gently.\n\nSome students hold tension in their jaw, neck, or shoulders while practicing Ujjayi. Regularly check that your face is relaxed and your shoulders are soft. The only engagement should be the subtle constriction at the back of the throat."
            },
            {
                "heading": "Beyond the Mat",
                "text": "While Ujjayi is primarily practiced during asana, its benefits extend beyond your yoga mat. Use this breath during meditation to maintain focus, or employ it during stressful moments in daily life to activate your relaxation response.\n\nA few rounds of Ujjayi breath before an important meeting, difficult conversation, or challenging task can center your mind and calm your nervous system. This ancient technique becomes a portable tool for maintaining equanimity amid life's demands."
            }
        ],
        "days_ago": 9
    },

    # BLOG 15 - Disease Cure
    {
        "title": "Yoga for Anxiety and Depression: A Holistic Approach to Mental Health",
        "excerpt": "Discover how yoga can be a powerful complement to traditional mental health treatment. Learn specific practices that help regulate mood, reduce anxiety, and foster emotional resilience.",
        "category": "Disease Cure",
        "category_color": "#95e1d3",
        "author": "Dr. Jennifer Lee, PhD",
        "read_time": "12 min read",
        "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "The Mind-Body Connection",
            "How Yoga Helps Anxiety",
            "Yoga for Depression",
            "Recommended Practices",
            "Creating a Therapeutic Routine",
            "When to Seek Professional Help"
        ],
        "content": [
            {
                "heading": "The Mind-Body Connection",
                "text": "Mental health and physical health are inseparable. Anxiety and depression manifest not just as thoughts and emotions, but as physical sensations: tension, fatigue, changes in breath pattern, and altered nervous system functioning. Yoga addresses both dimensions simultaneously.\n\nResearch increasingly supports yoga as an effective complementary treatment for anxiety and depression. Studies show it can reduce symptoms, improve sleep, enhance emotional regulation, and increase overall quality of life when practiced regularly.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Therapeutic yoga practice"
            },
            {
                "heading": "How Yoga Helps Anxiety",
                "text": "Anxiety often involves an overactive sympathetic nervous system—the fight-or-flight response stuck in the 'on' position. Yoga's combination of gentle movement, controlled breathing, and mindfulness activates the parasympathetic nervous system, our rest-and-digest mode.\n\nBreathing practices are particularly powerful for anxiety. Extending the exhale longer than the inhale signals safety to the nervous system. Forward folds and gentle inversions also have calming effects, directing blood flow to the brain and encouraging introspection rather than external hypervigilance."
            },
            {
                "heading": "Yoga for Depression",
                "text": "Depression often involves low energy, negative thought patterns, and disconnection from the body. Energizing practices like Sun Salutations, backbends, and standing poses can help lift mood and combat lethargy, though it's important to start gently.\n\nYoga's emphasis on present-moment awareness interrupts rumination—the tendency to dwell on past regrets or future worries that characterizes depression. Regular practice builds a different relationship with thoughts and emotions, creating space between stimulus and response.",
                "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=800&h=600&fit=crop",
                "imageAlt": "Uplifting yoga poses"
            },
            {
                "heading": "Recommended Practices",
                "text": "For anxiety: Practice slow, grounding sequences with longer holds. Include lots of forward folds, hip openers, and restorative poses. End with extended Savasana. Breathing practices: extend exhales, try Nadi Shodhana, or simple counted breathing.\n\nFor depression: Include more energizing practices like Sun Salutations, gentle backbends, and standing poses to build energy and confidence. Balance this with calming practices. Avoid long meditations initially if they increase rumination; focus on movement meditation instead."
            },
            {
                "heading": "Creating a Therapeutic Routine",
                "text": "Consistency matters more than intensity. Even 15 minutes daily can make a significant difference. Morning practice can set a positive tone for the day, while evening practice helps process the day's stress and prepare for rest.\n\nBe compassionate with yourself. Some days you'll feel motivated; other days, just unrolling your mat is enough. Modify practices to match your current state rather than forcing yourself into a predetermined routine."
            },
            {
                "heading": "When to Seek Professional Help",
                "text": "While yoga is a valuable tool for mental health, it's not a replacement for professional treatment when needed. If you're experiencing persistent symptoms, having thoughts of self-harm, or finding daily functioning difficult, please reach out to a mental health professional.\n\nYoga works best as part of a comprehensive approach that might include therapy, medication, lifestyle changes, and social support. Many therapists now recommend yoga as a complement to traditional treatment, recognizing its unique benefits for mind-body healing."
            }
        ],
        "days_ago": 14
    },

    # BLOG 16 - Meditation  
    {
        "title": "Body Scan Meditation: Deep Relaxation and Body Awareness",
        "excerpt": "Learn the practice of body scan meditation, a powerful technique for releasing physical tension, developing body awareness, and cultivating present-moment attention.",
        "category": "Meditation",
        "category_color": "#a8e6cf",
        "author": "Dr. Michael Chen",
        "read_time": "8 min read",
        "image": "https://images.unsplash.com/photo-1447452001602-7090c7ab2db3?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "What is Body Scan Meditation?",
            "The Practice Technique",
            "Benefits for Mind and Body",
            "Handling Discomfort",
            "Integration with Yoga Practice"
        ],
        "content": [
            {
                "heading": "What is Body Scan Meditation?",
                "text": "Body scan meditation involves systematically directing attention through different parts of the body, observing sensations without judgment. This practice comes from the Vipassana tradition but has been adapted and popularized in secular contexts, particularly in MBSR (Mindfulness-Based Stress Reduction).\n\nThe body scan bridges concentration and insight meditation. It develops focused attention while simultaneously cultivating non-reactive awareness—observing sensations as they arise and pass without trying to change them.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Body scan meditation practice"
            },
            {
                "heading": "The Practice Technique",
                "text": "Lie down in Savasana or sit comfortably. Take a few deep breaths to settle. Begin by bringing attention to your toes. Notice any sensations—tingling, warmth, pressure, or perhaps numbness. Simply observe without judging or trying to change anything.\n\nSlowly move your attention up through feet, ankles, calves, knees, thighs, and so on, spending 20-30 seconds with each area. When your mind wanders, gently return attention to the body part you're scanning. Complete scans can take 20-45 minutes."
            },
            {
                "heading": "Benefits for Mind and Body",
                "text": "Regular body scan practice significantly reduces physical tension. Many people unknowingly hold chronic tension in shoulders, jaw, or abdomen. This practice brings awareness to these patterns, and awareness itself often leads to release.\n\nThe body scan also trains attention. Each time you notice your mind has wandered and bring it back, you're strengthening your concentration. This skill transfers to daily life, helping you stay present in conversations, work, and relationships.",
                "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=800&h=600&fit=crop",
                "imageAlt": "Deep relaxation practice"
            },
            {
                "heading": "Handling Discomfort",
                "text": "When you encounter areas of discomfort or pain during the scan, resist the urge to immediately shift position. First, breathe into that area and observe the sensation with curiosity. Often, discomfort has an emotional component—fear, resistance, or aversion—that intensifies the physical sensation.\n\nPractice allowing sensations to be present without needing to fix them. This doesn't mean enduring unbearable pain; if something genuinely needs adjustment, adjust mindfully. The key distinction is between reactive fixing and responsive caring."
            },
            {
                "heading": "Integration with Yoga Practice",
                "text": "The body scan pairs beautifully with yoga asana. Practice a body scan at the beginning of your yoga session to assess how your body feels today, or at the end to observe the effects of your practice.\n\nMany yoga classes conclude with a guided body scan during final Savasana. This helps students transition from the active practice into deep rest and marks a clear ending to the practice session, making it easier to carry that embodied awareness into the rest of the day."
            }
        ],
        "days_ago": 19
    },

    # BLOG 17 - Philosophy
    {
        "title": "Yoga Nidra: The Art of Conscious Sleep",
        "excerpt": "Discover Yoga Nidra, an ancient practice of deep relaxation that occurs between waking and sleeping. Learn how this 'yogic sleep' can reduce stress, improve sleep, and access deeper states of consciousness.",
        "category": "Philosophy",
        "category_color": "#ffd93d",
        "author": "Swami Satyananda",
        "read_time": "10 min read",
        "image": "https://images.unsplash.com/photo-1499209974431-9dddcece7f88?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Understanding Yoga Nidra",
            "The Five Koshas Journey",
            "Sankalpa: The Heart's Resolution",
            "Scientific Benefits",
            "How to Practice"
        ],
        "content": [
            {
                "heading": "Understanding Yoga Nidra",
                "text": "Yoga Nidra, meaning 'yogic sleep,' is a systematic method of inducing complete physical, mental, and emotional relaxation. During Yoga Nidra, consciousness hovers between waking and sleeping—you're deeply relaxed yet maintaining awareness. This state is sometimes called the hypnagogic state.\n\nUnlike sleep where you're unconscious, Yoga Nidra maintains a thread of awareness even as the body and mind release into profound rest. One hour of Yoga Nidra is said to be as restorative as four hours of conventional sleep.",
                "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=800&h=600&fit=crop",
                "imageAlt": "Yoga Nidra practice"
            },
            {
                "heading": "The Five Koshas Journey",
                "text": "Traditional Yoga Nidra moves systematically through the five koshas (sheaths): Annamaya (physical), Pranamaya (energetic), Manomaya (mental), Vijnanamaya (wisdom), and Anandamaya (bliss). Each stage involves specific techniques—body awareness, breath awareness, emotional awareness, witnessing, and finally, pure being.\n\nThis journey inward represents the yogic understanding that we are more than just our physical body or thoughts. By experiencing each layer, we access deeper dimensions of ourselves and eventually touch the unchanging awareness that underlies all experience."
            },
            {
                "heading": "Sankalpa: The Heart's Resolution",
                "text": "A key element of Yoga Nidra is the Sankalpa—a short, positive statement of intention planted at the beginning and end of practice. Unlike typical affirmations, Sankalpa is stated as already true: 'I am peaceful' rather than 'I will be peaceful.'\n\nThe deeply relaxed state achieved during Yoga Nidra makes the mind especially receptive to positive suggestions. Your Sankalpa, repeated regularly, gradually reshapes unconscious patterns and manifests positive changes in your life. Choose your Sankalpa carefully and keep it consistent for months or years.",
                "image": "https://images.unsplash.com/photo-1447452001602-7090c7ab2db3?w=800&h=600&fit=crop",
                "imageAlt": "Setting intentions in Yoga Nidra"
            },
            {
                "heading": "Scientific Benefits",
                "text": "Research shows Yoga Nidra reduces anxiety and depression, improves sleep quality, and helps with PTSD symptoms. Brain scans reveal increased alpha wave activity (associated with relaxation) and decreased beta waves (associated with active thinking).\n\nRegular practice can lower blood pressure, reduce chronic pain, and improve immune function. The practice also enhances creativity and problem-solving by allowing access to subconscious material that's usually blocked by the busy conscious mind."
            },
            {
                "heading": "How to Practice",
                "text": "Yoga Nidra is typically practiced lying down in Savasana, though you can sit if lying down causes you to fall asleep. Follow a recorded guide, as trying to remember the sequence defeats the purpose of deep relaxation.\n\nPractice at a time when you won't be disturbed for 20-45 minutes. Keep the room warm as body temperature drops during deep relaxation. It's fine to practice before bed, though traditionally it's done during the day to experience the unique state between waking and sleeping without actually sleeping."
            }
        ],
        "days_ago": 24
    },

    # BLOG 18 - YTT
    {
        "title": "The Business of Yoga: Building a Sustainable Teaching Career",
        "excerpt": "Passionate about yoga but wondering how to make it financially viable? Learn practical strategies for building a sustainable yoga teaching career that honors both your calling and your needs.",
        "category": "YTT",
        "category_color": "#6c5ce7",
        "author": "Amanda Rodriguez",
        "read_time": "13 min read",
        "image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "The Reality of Yoga Economics",
            "Diversifying Your Income Streams",
            "Building Your Student Base",
            "Setting Your Rates",
            "Marketing Your Services",
            "Avoiding Burnout"
        ],
        "content": [
            {
                "heading": "The Reality of Yoga Economics",
                "text": "Let's be honest: most yoga teachers don't earn a full-time living from teaching drop-in classes alone. Studio classes typically pay $25-75 per class, and it takes time to build a full schedule. Understanding this reality from the start helps you plan strategically rather than becoming disillusioned.\n\nHowever, many teachers do build thriving yoga careers by diversifying income streams, developing specializations, and treating their teaching as a business. With creativity and dedication, a sustainable yoga career is absolutely possible.",
                "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200&h=600&fit=crop",
                "imageAlt": "Yoga business planning"
            },
            {
                "heading": "Diversifying Your Income Streams",
                "text": "Successful yoga teachers typically have multiple revenue sources: studio classes, private sessions, workshops, retreats, online classes, teacher training, corporate yoga, therapeutic sessions, and sometimes related offerings like massage, health coaching, or wellness consulting.\n\nPrivate sessions usually command higher rates ($75-150+ per hour) and allow you to work more personally with students. Workshops and retreats provide intensive, higher-value experiences. Online offerings create passive income and expand your reach beyond your local area."
            },
            {
                "heading": "Building Your Student Base",
                "text": "Your most valuable asset is your reputation and relationships. Show up consistently, be punctual, continue learning, and genuinely care about your students. Word-of-mouth remains the most powerful marketing tool in yoga.\n\nStart by subbing classes, teaching for free or donation-based in community spaces, or offering classes through gyms and studios. As you build experience and following, you can add private clients, create your own classes, or develop specialized programs.",
                "image": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&h=600&fit=crop",
                "imageAlt": "Building yoga community"
            },
            {
                "heading": "Setting Your Rates",
                "text": "Research local market rates but don't automatically price yourself at the bottom. Your rates should reflect your experience, specializations, and the value you provide. Remember, students who value quality instruction are willing to pay appropriately.\n\nFor private sessions, consider your expenses (studio rent, insurance, continuing education, travel) and the value of your time, including prep and administrative work. Don't forget to account for self-employment taxes and lack of benefits when calculating rates."
            },
            {
                "heading": "Marketing Your Services",
                "text": "In today's world, online presence is essential. Create a simple website and maintain active social media with authentic content—not just selfies in poses, but genuine insights, tips, and connection with your community.\n\nEmail lists remain highly effective for staying connected with students and promoting workshops or new offerings. Offer valuable free content to build your list. Collaborate with other wellness professionals for cross-promotion. Network genuinely rather than just trying to get students."
            },
            {
                "heading": "Avoiding Burnout",
                "text": "Teaching many classes weekly while maintaining your own practice, continuing education, and personal life can lead to exhaustion. Build rest into your schedule. Remember, you can't pour from an empty cup—your own practice and self-care directly impact your teaching quality.\n\nSet boundaries around your time and energy. It's okay to say no to opportunities that don't align with your values or compensate fairly. As you build your career, gradually move toward opportunities that are more fulfilling and sustainable rather than taking every possible gig."
            }
        ],
        "days_ago": 33
    },

    # BLOG 19 - Asanas
    {
        "title": "Hip Opening Sequences: Release Tension and Find Freedom",
        "excerpt": "Our hips store emotional and physical tension. Learn comprehensive hip opening sequences that safely increase flexibility, release stored stress, and create a sense of spaciousness in body and mind.",
        "category": "Asanas",
        "category_color": "#ff6b35",
        "author": "Deepak Sharma",
        "read_time": "10 min read",
        "image": "https://images.unsplash.com/photo-1588286840104-8957b019727f?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Why Hip Flexibility Matters",
            "Understanding Hip Anatomy",
            "Gentle Hip Opening Sequence",
            "Emotional Release in Hip Openers",
            "Daily Hip Care"
        ],
        "content": [
            {
                "heading": "Why Hip Flexibility Matters",
                "text": "Tight hips are ubiquitous in modern life. Prolonged sitting shortens hip flexors and weakens gluteal muscles. This imbalance contributes to lower back pain, poor posture, and reduced athletic performance. Beyond physical impacts, restricted hips can limit our sense of freedom and ease in the body.\n\nYoga hip openers systematically address these issues, creating balance between strength and flexibility. They prepare the body for deeper postures like lotus or splits, but more importantly, they help us move through daily life with greater comfort and range of motion.",
                "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200&h=600&fit=crop",
                "imageAlt": "Hip opening yoga sequence"
            },
            {
                "heading": "Understanding Hip Anatomy",
                "text": "The hip is a ball-and-socket joint capable of movement in multiple directions: flexion/extension, abduction/adduction, and internal/external rotation. Comprehensive hip opening addresses all these ranges of motion rather than just focusing on one direction.\n\nMajor muscles affecting hip mobility include hip flexors (psoas, rectus femoris), extensors (glutes, hamstrings), adductors (inner thigh), and external rotators (piriformis and others). Different poses target different muscle groups, so variety in your practice is key."
            },
            {
                "heading": "Gentle Hip Opening Sequence",
                "text": "Begin with Reclined Figure Four to gently introduce external rotation. Hold 2-3 minutes per side. Move to Happy Baby for inner thigh release. Transition to Low Lunge for hip flexor opening, optionally moving into Lizard Pose for deeper work in the hip socket.\n\nInclude Pigeon Pose (or Reclined Pigeon for beginners) for intense external rotator work. Thread the Needle from all fours offers similar benefits with less intensity. Finish with wide-legged forward fold to release inner thighs. Always move slowly and never force your body into hip openers.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Pigeon pose for hip opening"
            },
            {
                "heading": "Emotional Release in Hip Openers",
                "text": "Many practitioners experience emotional release during deep hip work. This isn't coincidence—the psoas muscle connects to our fight-or-flight response, potentially storing trauma and stress. When we stretch these areas, we may access emotions we've been holding.\n\nIf emotions arise during hip openers, remember this is normal and healthy. Breathe through the feelings without judgment. Some days hip openers feel easy; other days they're intense. This variation reflects our ever-changing physical and emotional state."
            },
            {
                "heading": "Daily Hip Care",
                "text": "You don't need an hour-long practice to maintain hip health. Incorporate simple hip openers throughout your day: sit in squat position while waiting, take walking breaks from sitting, practice standing figure four while brushing teeth.\n\nConsistency matters more than intensity. Even 10 minutes of focused hip work daily will create more change than occasional long sessions. Your hips will gradually open if you're patient and regular in your practice, though progress isn't always linear. Honor your body's unique structure and timeline."
            }
        ],
        "days_ago": 6
    },

    # BLOG 20 - Pranayam
    {
        "title": "Breath Retention: Advanced Pranayama for Energy and Focus",
        "excerpt": "Explore the practice of breath retention (Kumbhaka) in pranayama. Learn how consciously holding the breath can increase lung capacity, mental clarity, and pranic energy when practiced safely and progressively.",
        "category": "Pranayam",
        "category_color": "#4ecdc4",
        "author": "Guru Narayan Das",
        "read_time": "9 min read",
        "image": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Understanding Kumbhaka",
            "Benefits of Breath Retention",
            "Antara and Bahya Kumbhaka",
            "Progressive Practice Guidelines",
            "Safety and Contraindications"
        ],
        "content": [
            {
                "heading": "Understanding Kumbhaka",
                "text": "Kumbhaka means 'breath retention' or 'breath suspension' in Sanskrit. While basic pranayama focuses on regulation of inhalation and exhalation, advanced practice includes the pause between breaths. This momentary stillness is said to be when prana (life force) is most effectively absorbed into the body.\n\nTraditional texts describe Kumbhaka as the true pranayama, with inhalation (Puraka) and exhalation (Rechaka) serving primarily to prepare for and support the retention. However, retention should only be practiced after establishing strong foundations in basic breathing exercises.",
                "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=800&h=600&fit=crop",
                "imageAlt": "Advanced pranayama practice"
            },
            {
                "heading": "Benefits of Breath Retention",
                "text": "Kumbhaka builds lung capacity and strengthens respiratory muscles. It increases cellular oxygenation and trains the body to use oxygen more efficiently. Many practitioners report increased mental clarity, focus, and a sense of inner stillness that extends beyond the practice itself.\n\nPhysiologically, retention triggers mild beneficial stress responses that, over time, increase resilience. The practice stimulates the vagus nerve, supporting emotional regulation and stress management. Energetically, retention is said to distribute prana throughout the energy channels of the body."
            },
            {
                "heading": "Antara and Bahya Kumbhaka",
                "text": "There are two types of retention: Antara Kumbhaka (retention after inhale) and Bahya Kumbhaka (retention after exhale). Each affects the body and mind differently.\n\nAntara Kumbhaka is energizing and warming, building heat and vitality. It strengthens the heart and lungs. Bahya Kumbhaka is calming and cooling, encouraging introspection and letting go. Many traditions emphasize Bahya Kumbhaka as particularly powerful for meditation, as the emptiness after exhale mirrors the spaciousness of pure awareness.",
                "image": "https://images.unsplash.com/photo-1593811167562-9cef47bfc4d7?w=800&h=600&fit=crop",
                "imageAlt": "Breath retention technique"
            },
            {
                "heading": "Progressive Practice Guidelines",
                "text": "Never force retention or hold to the point of gasping. Progress gradually over months and years. Start with a comfortable breath rhythm, perhaps 4 counts in, 4 counts out. Once this feels easy, add 1-2 count retention: 4 in, 2 hold, 4 out. Slowly increase retention time while keeping inhalation and exhalation comfortable.\n\nA classical ratio is 1:4:2 (if you inhale for 4, hold for 16, exhale for 8). But this takes years to achieve safely. Don't rush. The practice should feel steady and sustainable, never strained. Work with a qualified teacher when developing retention practice."
            },
            {
                "heading": "Safety and Contraindications",
                "text": "Breath retention is contraindicated for people with high blood pressure, heart conditions, or pregnancy. Those with anxiety or panic disorder should approach cautiously, as retention can sometimes trigger panic. If you experience dizziness, rapid heartbeat, or anxiety, stop immediately.\n\nPractice on an empty stomach, ideally in the morning. Create a calm, quiet environment. If you're new to pranayama, spend months establishing basic breathing practices before introducing retention. Remember, in yoga we progress slowly and steadily rather than pushing for dramatic breakthroughs that might compromise safety."
            }
        ],
        "days_ago": 11
    },

    # BLOG 21 - Disease Cure
    {
        "title": "Yoga for Digestive Health: Poses and Practices for Optimal Gut Function",
        "excerpt": "Digestive issues affect millions. Discover specific yoga poses, breathing practices, and lifestyle adjustments that support healthy digestion, reduce bloating, and address common gut problems naturally.",
        "category": "Disease Cure",
        "category_color": "#95e1d3",
        "author": "Dr. Priya Malhotra",
        "read_time": "11 min read",
        "image": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=1200&h=600&fit=crop",
        "table_of_contents": [
            "Understanding Digestive Issues",
            "How Yoga Supports Digestion",
            "Poses for Digestive Health",
            "Pranayama and the Vagus Nerve",
            "Ayurvedic Perspectives",
            "Lifestyle and Dietary Considerations"
        ],
        "content": [
            {
                "heading": "Understanding Digestive Issues",
                "text": "Digestive complaints—bloating, constipation, IBS, acid reflux—are incredibly common in our modern world. Stress, processed foods, irregular eating patterns, and sedentary lifestyles all contribute to digestive dysfunction. While yoga isn't a cure-all, it addresses many of these root causes.\n\nThe gut-brain connection means that our mental and emotional states directly affect digestion. Stress triggers the sympathetic nervous system, which shuts down digestive processes. This is why nervous situations can cause digestive upset, and why relaxation practices support gut health.",
                "image": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=1200&h=600&fit=crop",
                "imageAlt": "Yoga for digestive wellness"
            },
            {
                "heading": "How Yoga Supports Digestion",
                "text": "Physical poses massage internal organs, stimulating digestion and encouraging elimination. Twists particularly support digestive health by wringing out organs and promoting movement through the intestines. Forward folds compress the abdomen, while backbends create space.\n\nBeyond physical benefits, yoga's stress-reduction effects allow the parasympathetic nervous system—responsible for rest and digest—to function optimally. Regular practice can help regulate bowel movements, reduce inflammation, and improve nutrient absorption."
            },
            {
                "heading": "Poses for Digestive Health",
                "text": "Pavanamuktasana (Wind-Relieving Pose) is specifically designed to release gas and bloating. Lying on your back, draw one or both knees to chest. Apanasana (Knees-to-Chest Pose) provides similar benefits with a gentle rocking motion.\n\nTwists like Seated Spinal Twist, Revolved Triangle, or Supine Twist stimulate peristalsis. Cat-Cow sequence massages organs with its undulating movement. Legs-Up-the-Wall pose reverses blood flow and can help with elimination. Practice these poses consistently, especially in morning to encourage regularity.",
                "image": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?w=800&h=600&fit=crop",
                "imageAlt": "Twisting poses for digestion"
            },
            {
                "heading": "Pranayama and the Vagus Nerve",
                "text": "The vagus nerve runs from the brainstem through the organs, including the entire digestive tract. It's the main component of the parasympathetic nervous system. Slow, diaphragmatic breathing stimulates the vagus nerve, promoting the relaxation response needed for optimal digestion.\n\nPractice belly breathing: place one hand on chest, one on belly. Breathe so only the belly hand moves. This engages the diaphragm, which massages internal organs while activating the vagus nerve. Practice 5-10 minutes daily, especially before meals."
            },
            {
                "heading": "Ayurvedic Perspectives",
                "text": "Ayurveda, yoga's sister science, emphasizes 'Agni' or digestive fire. Morning practice is ideal as it kindles Agni for the day ahead. Inverted poses are generally avoided right after eating, as they work against natural digestive flow.\n\nAyurveda recommends the largest meal at midday when Agni is strongest. Warm, cooked foods are easier to digest than raw, cold foods. Eating in a calm environment without distraction supports better digestion—a practice that complements yoga's emphasis on mindfulness."
            },
            {
                "heading": "Lifestyle and Dietary Considerations",
                "text": "While yoga helps digestive health, it works best combined with supportive lifestyle choices. Eat regular meals at consistent times. Stay hydrated but avoid drinking large amounts with meals, which dilutes digestive enzymes. Chew food thoroughly—digestion begins in the mouth.\n\nManage stress through regular yoga and meditation. Exercise daily but not immediately after large meals. Pay attention to how different foods affect you—food sensitivities are individual. Consider keeping a food diary to identify patterns between what you eat and how you feel."
            }
        ],
        "days_ago": 16
    }
]

def seed_blogs():
    db = SessionLocal()
    
    try:
        # Clear existing blogs (optional - comment out if you want to keep existing data)
        print("🗑️  Clearing existing blogs...")
        db.query(Blog).delete()
        db.commit()
        
        print(f"🌱 Seeding {len(SAMPLE_BLOGS)} blogs...")
        
        for blog_data in SAMPLE_BLOGS:
            days_ago = blog_data.pop('days_ago', 0)
            created_date = datetime.utcnow() - timedelta(days=days_ago)
            
            # Generate slug
            slug = Blog.generate_slug(blog_data['title'])
            
            # Check if slug already exists
            existing = db.query(Blog).filter(Blog.slug == slug).first()
            if existing:
                counter = 1
                while db.query(Blog).filter(Blog.slug == f"{slug}-{counter}").first():
                    counter += 1
                slug = f"{slug}-{counter}"
            
            blog = Blog(
                slug=slug,
                title=blog_data['title'],
                excerpt=blog_data['excerpt'],
                category=blog_data['category'],
                category_color=blog_data['category_color'],
                author=blog_data['author'],
                read_time=blog_data['read_time'],
                image=blog_data['image'],
                table_of_contents=blog_data['table_of_contents'],
                content=blog_data['content'],
                published=True,
                created_at=created_date,
                updated_at=created_date
            )
            
            db.add(blog)
        
        db.commit()
        print(f"\n🎉 Successfully seeded {len(SAMPLE_BLOGS)} blogs!")
        
        # Show category distribution
        print("\n📊 Category Distribution:")
        for category in ["Asanas", "Pranayam", "Disease Cure", "Meditation", "Philosophy", "YTT"]:
            count = sum(1 for b in SAMPLE_BLOGS if b['category'] == category)
            print(f"  {category}: {count} blogs")
        
    except Exception as e:
        print(f"❌ Error seeding blogs: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_blogs()
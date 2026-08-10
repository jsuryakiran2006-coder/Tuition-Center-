from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>BrightMind Academy | Maths & Science</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, Helvetica, sans-serif;
            scroll-behavior: smooth;
        }

        body {
            background: #f7f9fc;
            color: #1f2937;
        }

        /* NAVBAR */

        nav {
            position: sticky;
            top: 0;
            z-index: 1000;

            display: flex;
            justify-content: space-between;
            align-items: center;

            padding: 18px 8%;

            background: white;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        }

        .logo {
            font-size: 25px;
            font-weight: bold;
            color: #2563eb;
        }

        .logo span {
            color: #111827;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 30px;
        }

        nav a {
            text-decoration: none;
            color: #374151;
            font-weight: 600;
        }

        nav a:hover {
            color: #2563eb;
        }

        /* HERO */

        .hero {
            min-height: 600px;

            display: flex;
            align-items: center;

            padding: 80px 8%;

            background:
                linear-gradient(
                    120deg,
                    #eff6ff,
                    #ffffff
                );
        }

        .hero-content {
            max-width: 650px;
        }

        .badge {
            display: inline-block;

            background: #dbeafe;
            color: #2563eb;

            padding: 8px 15px;
            border-radius: 20px;

            font-size: 14px;
            font-weight: bold;

            margin-bottom: 20px;
        }

        .hero h1 {
            font-size: 58px;
            line-height: 1.1;
            margin-bottom: 20px;
            color: #111827;
        }

        .hero h1 span {
            color: #2563eb;
        }

        .hero p {
            font-size: 19px;
            line-height: 1.7;
            color: #6b7280;
            margin-bottom: 30px;
        }

        .buttons {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-block;

            padding: 14px 25px;

            border-radius: 8px;

            text-decoration: none;

            font-weight: bold;

            transition: 0.3s;
        }

        .primary {
            background: #2563eb;
            color: white;
        }

        .primary:hover {
            background: #1d4ed8;
            transform: translateY(-2px);
        }

        .secondary {
            border: 2px solid #2563eb;
            color: #2563eb;
        }

        .secondary:hover {
            background: #2563eb;
            color: white;
        }

        /* STATS */

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);

            max-width: 900px;

            margin: -50px auto 0;

            position: relative;

            background: white;

            border-radius: 15px;

            box-shadow: 0 8px 30px rgba(0,0,0,0.08);
        }

        .stat {
            text-align: center;
            padding: 30px;
        }

        .stat h2 {
            color: #2563eb;
            font-size: 30px;
        }

        .stat p {
            color: #6b7280;
            margin-top: 5px;
        }

        /* GENERAL */

        section {
            padding: 90px 8%;
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }

        .section-title h2 {
            font-size: 38px;
            color: #111827;
            margin-bottom: 10px;
        }

        .section-title p {
            color: #6b7280;
            font-size: 17px;
        }

        /* COURSES */

        .courses {
            display: grid;

            grid-template-columns:
                repeat(2, minmax(250px, 1fr));

            gap: 30px;

            max-width: 1000px;

            margin: auto;
        }

        .course {
            background: white;

            padding: 35px;

            border-radius: 18px;

            box-shadow:
                0 8px 30px rgba(0,0,0,0.07);

            transition: 0.3s;

            border-top: 5px solid #2563eb;
        }

        .course:hover {
            transform: translateY(-8px);
        }

        .course-icon {
            font-size: 45px;
            margin-bottom: 20px;
        }

        .course h3 {
            font-size: 27px;
            margin-bottom: 15px;
        }

        .course p {
            color: #6b7280;
            line-height: 1.7;
            margin-bottom: 20px;
        }

        .course ul {
            list-style: none;
        }

        .course li {
            margin: 10px 0;
        }

        .course li::before {
            content: "✓";
            color: #2563eb;
            font-weight: bold;
            margin-right: 10px;
        }

        /* ONLINE CLASSES */

        .online {
            background: #111827;
            color: white;

            border-radius: 25px;

            max-width: 1100px;

            margin: auto;

            padding: 60px;
        }

        .online-content {
            display: grid;
            grid-template-columns: 1fr 1fr;

            gap: 50px;

            align-items: center;
        }

        .online h2 {
            font-size: 40px;
            margin-bottom: 20px;
        }

        .online p {
            color: #d1d5db;
            line-height: 1.7;
        }

        .online-badge {
            display: inline-block;

            background: #16a34a;

            padding: 8px 14px;

            border-radius: 20px;

            font-size: 13px;

            margin-bottom: 20px;
        }

        .schedule {
            background: white;
            color: #111827;

            border-radius: 15px;

            padding: 25px;
        }

        .schedule h3 {
            margin-bottom: 20px;
        }

        .class-row {
            display: flex;
            justify-content: space-between;

            padding: 15px 0;

            border-bottom: 1px solid #e5e7eb;
        }

        .class-row:last-child {
            border-bottom: none;
        }

        .available {
            color: #16a34a;
            font-weight: bold;
        }

        /* WHY US */

        .features {
            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 25px;

            max-width: 1100px;

            margin: auto;
        }

        .feature {
            background: white;

            padding: 30px;

            border-radius: 15px;

            text-align: center;

            box-shadow: 0 5px 20px rgba(0,0,0,0.06);
        }

        .feature-icon {
            font-size: 35px;
            margin-bottom: 15px;
        }

        .feature h3 {
            margin-bottom: 10px;
        }

        .feature p {
            color: #6b7280;
            line-height: 1.6;
        }

        /* CONTACT */

        .contact {
            background: #eff6ff;
        }

        .contact-box {
            max-width: 850px;

            margin: auto;

            text-align: center;
        }

        .contact-box h2 {
            font-size: 38px;
            margin-bottom: 15px;
        }

        .contact-box p {
            color: #6b7280;
            margin-bottom: 25px;
        }

        .contact-info {
            display: flex;

            justify-content: center;

            gap: 40px;

            flex-wrap: wrap;

            margin-top: 30px;
        }

        /* FOOTER */

        footer {
            background: #111827;

            color: white;

            text-align: center;

            padding: 30px;
        }

        footer p {
            color: #9ca3af;
            margin-top: 8px;
        }

        /* MOBILE */

        @media(max-width: 768px) {

            nav {
                padding: 15px 5%;
            }

            nav ul {
                display: none;
            }

            .hero {
                min-height: 500px;
                padding: 60px 6%;
            }

            .hero h1 {
                font-size: 40px;
            }

            .stats {
                width: 90%;
                grid-template-columns: 1fr;
                margin-top: 20px;
            }

            .courses {
                grid-template-columns: 1fr;
            }

            .online-content {
                grid-template-columns: 1fr;
            }

            .online {
                padding: 30px;
            }

            .features {
                grid-template-columns: 1fr;
            }

            section {
                padding: 60px 6%;
            }
        }

    </style>
</head>

<body>

<!-- NAVIGATION -->

<nav>

    <div class="logo">
        Bright<span>Mind</span>
    </div>

    <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#courses">Courses</a></li>
        <li><a href="#online">Online Classes</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>

</nav>


<!-- HERO -->

<section class="hero" id="home">

    <div class="hero-content">

        <div class="badge">
            🎓 Classes 8 - 12
        </div>

        <h1>
            Master <span>Maths</span> & Science
        </h1>

        <p>
            Build strong concepts, improve your problem-solving skills
            and prepare confidently for your school examinations with
            expert guidance.
        </p>

        <div class="buttons">

            <a href="#contact" class="btn primary">
                Book Free Demo
            </a>

            <a href="#courses" class="btn secondary">
                Explore Courses
            </a>

        </div>

    </div>

</section>


<!-- STATS -->

<div class="stats">

    <div class="stat">
        <h2>8 - 12</h2>
        <p>Classes</p>
    </div>

    <div class="stat">
        <h2>2</h2>
        <p>Core Subjects</p>
    </div>

    <div class="stat">
        <h2>Online</h2>
        <p>Classes Available</p>
    </div>

</div>


<!-- COURSES -->

<section id="courses">

    <div class="section-title">

        <h2>Our Courses</h2>

        <p>
            Focused learning for high school students
        </p>

    </div>


    <div class="courses">

        <!-- MATHS -->

        <div class="course">

            <div class="course-icon">
                🧮
            </div>

            <h3>Mathematics</h3>

            <p>
                Understand mathematical concepts instead of
                simply memorizing formulas.
            </p>

            <ul>

                <li>Algebra</li>

                <li>Geometry</li>

                <li>Trigonometry</li>

                <li>Statistics</li>

                <li>Problem Solving</li>

                <li>Exam Preparation</li>

            </ul>

        </div>


        <!-- SCIENCE -->

        <div class="course">

            <div class="course-icon">
                🔬
            </div>

            <h3>Science</h3>

            <p>
                Learn science through concepts, examples,
                experiments and real-world applications.
            </p>

            <ul>

                <li>Physics</li>

                <li>Chemistry</li>

                <li>Biology</li>

                <li>Important Diagrams</li>

                <li>Numerical Problems</li>

                <li>Exam Preparation</li>

            </ul>

        </div>

    </div>

</section>


<!-- ONLINE CLASSES -->

<section id="online">

    <div class="online">

        <div class="online-content">

            <div>

                <div class="online-badge">
                    ● ONLINE CLASSES AVAILABLE
                </div>

                <h2>
                    Learn From Anywhere
                </h2>

                <p>
                    Can't attend physical classes?
                    No problem. Join our live online classes
                    from your home using your laptop, tablet
                    or smartphone.
                </p>

                <br>

                <p>
                    ✓ Live interactive classes<br>
                    ✓ Doubt clearing sessions<br>
                    ✓ Digital study materials<br>
                    ✓ Recorded revision sessions
                </p>

            </div>


            <div class="schedule">

                <h3>
                    📅 Online Class Schedule
                </h3>

                <div class="class-row">

                    <span>Mathematics</span>

                    <span class="available">
                        Mon & Wed
                    </span>

                </div>

                <div class="class-row">

                    <span>Science</span>

                    <span class="available">
                        Tue & Thu
                    </span>

                </div>

                <div class="class-row">

                    <span>Revision Class</span>

                    <span class="available">
                        Saturday
                    </span>

                </div>

                <div class="class-row">

                    <span>Demo Class</span>

                    <span class="available">
                        Available
                    </span>

                </div>

            </div>

        </div>

    </div>

</section>


<!-- WHY CHOOSE US -->

<section>

    <div class="section-title">

        <h2>Why Choose BrightMind?</h2>

        <p>
            More than just tuition — we help students understand.
        </p>

    </div>


    <div class="features">

        <div class="feature">

            <div class="feature-icon">
                👨‍🏫
            </div>

            <h3>
                Expert Teaching
            </h3>

            <p>
                Experienced teachers who focus on
                understanding concepts clearly.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon">
                📝
            </div>

            <h3>
                Regular Tests
            </h3>

            <p>
                Practice tests and assessments help
                students track their progress.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon">
                💡
            </div>

            <h3>
                Doubt Clearing
            </h3>

            <p>
                Students can ask questions and get
                individual guidance whenever needed.
            </p>

        </div>

    </div>

</section>


<!-- CONTACT -->

<section class="contact" id="contact">

    <div class="contact-box">

        <h2>
            Ready to Improve Your Grades?
        </h2>

        <p>
            Book a free demo class and experience
            our teaching methodology.
        </p>

        <a href="mailto:sudheenajyothi@gmail.com"
           class="btn primary">
            Book Free Demo
        </a>

        <div class="contact-info">

            <div>
                📞 +91 6238036446
            </div>

            <div>
                📧 sudheenajyothi@gmail.com
            </div>

            <div>
                📍 Surya Nivas, S H Lane, Vyttila
            </div>

        </div>

    </div>

</section>


<!-- FOOTER -->

<footer>

    <strong>
        BrightMind Academy
    </strong>

    <p>
        Maths & Science Tuition for High School Students
    </p>

    <p>
        © 2026 BrightMind Academy. All Rights Reserved.
    </p>

</footer>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)
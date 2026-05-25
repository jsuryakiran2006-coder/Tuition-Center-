# app.py
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bright Future Tuition Center</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: Arial, sans-serif;
        }

        body{
            background:#f4f7fb;
            color:#333;
        }

        header{
            background:#1e3a8a;
            color:white;
            padding:20px;
            text-align:center;
        }

        nav{
            background:#2563eb;
            padding:10px;
            text-align:center;
        }

        nav a{
            color:white;
            text-decoration:none;
            margin:0 15px;
            font-weight:bold;
        }

        .hero{
            height:400px;
            background:linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
            url('https://images.unsplash.com/photo-1509062522246-3755977927d7');
            background-size:cover;
            background-position:center;
            display:flex;
            justify-content:center;
            align-items:center;
            text-align:center;
            color:white;
            padding:20px;
        }

        .hero h1{
            font-size:50px;
            margin-bottom:15px;
        }

        .hero p{
            font-size:20px;
        }

        .container{
            width:90%;
            max-width:1200px;
            margin:auto;
            padding:50px 0;
        }

        .subjects{
            display:grid;
            grid-template-columns:repeat(auto-fit, minmax(250px,1fr));
            gap:20px;
        }

        .card{
            background:white;
            padding:25px;
            border-radius:10px;
            box-shadow:0 4px 10px rgba(0,0,0,0.1);
            transition:0.3s;
        }

        .card:hover{
            transform:translateY(-5px);
        }

        .card h3{
            color:#1e3a8a;
            margin-bottom:10px;
        }

        .about{
            background:white;
            padding:40px;
            border-radius:10px;
            margin-top:40px;
            box-shadow:0 4px 10px rgba(0,0,0,0.1);
        }

        .contact{
            margin-top:40px;
            background:#1e3a8a;
            color:white;
            padding:40px;
            border-radius:10px;
        }

        footer{
            text-align:center;
            background:#111827;
            color:white;
            padding:15px;
            margin-top:40px;
        }

        button{
            background:#f59e0b;
            color:white;
            border:none;
            padding:12px 20px;
            border-radius:5px;
            font-size:16px;
            cursor:pointer;
            margin-top:20px;
        }

        button:hover{
            background:#d97706;
        }
    </style>
</head>
<body>

    <header>
        <h1>Bright Future Tuition Center</h1>
        <p>Math & Science Coaching for High School Students</p>
    </header>

    <nav>
        <a href="#subjects">Subjects</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
    </nav>

    <section class="hero">
        <div>
            <h1>Learn. Practice. Excel.</h1>
            <p>Expert guidance in Mathematics and Science for Classes 8 - 12</p>
            <button onclick="showMessage()">Join Now</button>
        </div>
    </section>

    <div class="container">

        <section id="subjects">
            <h2 style="text-align:center; margin-bottom:30px;">Our Subjects</h2>

            <div class="subjects">

                <div class="card">
                    <h3>Mathematics</h3>
                    <p>
                        Algebra, Geometry, Trigonometry, Calculus,
                        Problem Solving, Exam Preparation.
                    </p>
                </div>

                <div class="card">
                    <h3>Physics</h3>
                    <p>
                        Motion, Electricity, Magnetism, Optics,
                        Numerical Problems and Lab Concepts.
                    </p>
                </div>

                <div class="card">
                    <h3>Chemistry</h3>
                    <p>
                        Organic Chemistry, Chemical Reactions,
                        Periodic Table and Practical Applications.
                    </p>
                </div>

                <div class="card">
                    <h3>Biology</h3>
                    <p>
                        Human Body, Genetics, Ecology,
                        Diagrams and Scientific Understanding.
                    </p>
                </div>

            </div>
        </section>

        <section id="about" class="about">
            <h2>About Us</h2>
            <br>
            <p>
                Bright Future Tuition Center provides high-quality coaching
                for high school students. We focus on concept clarity,
                regular tests, doubt clearing sessions, and personalized guidance
                to help students achieve academic success.
            </p>
        </section>

        <section id="contact" class="contact">
            <h2>Contact Us</h2>
            <br>
            <p><strong>Phone:</strong> +91 6238036446</p>
            <p><strong>Email:</strong> sudheenajyothi@gmail.com</p>
            <p><strong>Location:</strong> <a href="https://maps.app.goo.gl/7us1Hf7xJpSLqyU87" target="_blank" style="color:white;">VRA 250 ,Surya Nivas, Safdar Hashmi Lane, Vytiila, Kochi, Kerala</a></p>
        </section>

    </div>

    <footer>
        <p>© 2026 Bright Future Tuition Center | All Rights Reserved</p>
    </footer>

    <script>
        function showMessage(){
            alert("Thank you for your interest! Contact us to enroll.");
        }
    </script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(debug=True)
THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora&family=Nunito&display=swap');

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

body {
    background: #f7f3ec;
    font-family: 'Nunito', sans-serif;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #f2ede4;
    border-right: 1px solid #ddd;
}

/* HERO */
.hero-title {
    font-size: 48px;
    font-family: 'Lora', serif;
    color: #2c3e28;
}

.hero-sub {
    color: #7a6e60;
}

/* STATS */
.stat {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #eee;
    text-align: center;
}

.stat b {
    font-size: 22px;
    color: #3a5c38;
}

/* CARDS */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    transition: 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0px 10px 25px rgba(0,0,0,0.1);
}
</style>
"""
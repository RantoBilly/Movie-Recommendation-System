// script.js

document.getElementById('movie-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const movieTitle = document.getElementById('movie-input').value;
    const recommendationsDiv = document.getElementById('recommendations');

    recommendationsDiv.innerHTML = ''; // clearing the previous results

    try {
        const response = await fetch ('http://localhost:8000/recommend/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({title: movieTitle}),
        });

        if (!response.ok) {
            throw new Error('Error Network');
        }

        const recommendations = await response.json();

        if (recommendations.length === 0) {
            recommendationsDiv.innerHTML = '<p>No recommendation found.</p>';
            return ;
        }

        recommendations.forEach(movie => {
            const movieItem = document.createElement('div');
            movieItem.className = 'recommendation-item';

            const movieTitle = document.createElement('h3');
            movieTitle.textContent = movie.title;

            const moviePoster = document.createElement('img');
            moviePoster.src = movie.poster_url;
            moviePoster.alt = movie.title;

            movieItem.appendChild(moviePoster);
            movieItem.appendChild(movieTitle);
            recommendationsDiv.appendChild(movieItem);
        });

    } catch (error) {
        console.error('Error fetching recommendations', error);
        recommendationsDiv.innerHTML = '<p>An error occured while recommendations</p>';
    }
})
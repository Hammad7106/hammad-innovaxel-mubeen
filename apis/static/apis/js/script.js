document.addEventListener('DOMContentLoaded', function () {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    document.getElementById('shortenForm').addEventListener('submit', async function (e) {
        e.preventDefault();
        const formData = new FormData(e.target);
        const originalUrl = formData.get('original_url');

        try {
            const response = await fetch('/shorten/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ original_url: originalUrl }),
            });

            if (response.ok) {
                const data = await response.json();
                document.getElementById('result').innerHTML = `
                    <p>Short URL created successfully!</p>
                    <p>Original URL: <a href="${data.original_url}" target="_blank">${data.original_url}</a></p>
                    <p>Short URL: <a href="/${data.short_code}" target="_blank">/${data.short_code}</a></p>
                `;
            } else {
                const error = await response.json();
                document.getElementById('result').innerHTML = `<p>Error: ${error.error}</p>`;
            }
        } catch (error) {
            document.getElementById('result').innerHTML = `<p>Error: ${error.message}</p>`;
        }
    });
});

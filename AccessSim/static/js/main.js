const form = document.getElementById("form-lead");
const message = document.getElementById("form-message");

function scrollToComponent(component_id) {
    const component = document.getElementById(component_id);
    component?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function showMessage(text, isSuccess) {
    if (!message) {
        return;
    }

    message.textContent = text;
    message.className = isSuccess ? 'success' : 'error';
    message.style.display = 'block';
}

if (form) {
    form.addEventListener('submit', async function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const csrfToken = formData.get('csrfmiddlewaretoken');

        try {
            const response = await fetch(form.action || window.location.href, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': csrfToken || '',
                }
            });

            const responseText = await response.text();
            let data = {};

            if (responseText) {
                try {
                    data = JSON.parse(responseText);
                } catch (error) {
                    console.error('Invalid JSON response', error);
                    data = {
                        success: false,
                        message: 'Ouve um erro de comunicação com o servidor.',
                    };
                }
            }

            if (data.success) {
                showMessage(data.message, true);
                form.reset();
            } else {
                showMessage(data.message || 'Há erros nos valores do formulário.', false);

                for (let field in data.errors || {}) {
                    const errorElement = document.getElementById('error-' + field);

                    if (errorElement) {
                        errorElement.textContent = data.errors[field].join(', ');
                    }
                }
            }
        } catch (error) {
            showMessage('Ouve um erro de comunicação com o servidor.', false);
            console.error(error);
        }
    });
}

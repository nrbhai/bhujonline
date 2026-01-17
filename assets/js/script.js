// script.js

document.addEventListener('DOMContentLoaded', () => {
    // Detect which page we're on based on DOM elements, not URL
    // This works with Cloudflare Pages' pretty URLs (/category instead of /category.html)

    if (document.getElementById('category-list')) {
        // Home page has category-list element
        initHomePage();
    } else if (document.getElementById('provider-list')) {
        // Category page has provider-list element
        initCategoryPage();
    }
});

function initHomePage() {
    const listContainer = document.getElementById('category-list');
    const searchInput = document.getElementById('home-search');
    if (!listContainer) return;

    const allCategories = window.getAllCategories();

    // Sort categories alphabetically
    allCategories.sort((a, b) => a.name.localeCompare(b.name));

    const render = (categories) => {
        if (categories.length === 0) {
            listContainer.innerHTML = '<li class="empty-state">No categories found.</li>';
            return;
        }

        const html = categories.map(cat => `
            <li>
                <a href="category.html?id=${cat.id}">
                    <span class="cat-icon">${cat.icon}</span>
                    <span class="cat-text">
                        <span class="cat-name-en">${cat.name}</span>
                        <span class="cat-name-gu">${cat.gu_name}</span>
                    </span>
                </a>
            </li>
        `).join('');

        listContainer.innerHTML = html;
    };

    // Initial render
    render(allCategories);

    // Search functionality
    if (searchInput) {
        // Mobile optimization: Add search-active class on focus
        searchInput.addEventListener('focus', () => {
            if (window.innerWidth <= 600) {
                document.body.classList.add('search-active');
            }
        });

        // Remove search-active class when user scrolls or clicks outside
        searchInput.addEventListener('blur', () => {
            // Small delay to allow click events to process
            setTimeout(() => {
                document.body.classList.remove('search-active');
            }, 200);
        });

        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            const filtered = allCategories.filter(cat =>
                cat.name.toLowerCase().includes(query) ||
                (cat.gu_name && cat.gu_name.includes(query))
            );
            render(filtered);
        });

        // Voice Search Implementation
        const voiceBtn = document.getElementById('voice-search-btn');
        
        if (voiceBtn) {
            // Check if browser supports speech recognition
            const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
            
            if (SpeechRecognition) {
                const recognition = new SpeechRecognition();
                recognition.continuous = false;
                recognition.interimResults = false;
                recognition.maxAlternatives = 1;
                
                // Support both English and Gujarati
                recognition.lang = 'en-IN';
                
                let isListening = false;
                
                voiceBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    if (isListening) {
                        recognition.stop();
                        return;
                    }
                    
                    try {
                        recognition.start();
                        isListening = true;
                        voiceBtn.classList.add('listening');
                        searchInput.placeholder = 'Listening... 🎤';
                    } catch (error) {
                        console.error('Recognition start error:', error);
                        alert('Could not start voice recognition. Please try again.');
                    }
                });

                recognition.onresult = (event) => {
                    const transcript = event.results[0][0].transcript;
                    searchInput.value = transcript;
                    
                    // Trigger search
                    const inputEvent = new Event('input', { bubbles: true });
                    searchInput.dispatchEvent(inputEvent);
                    
                    isListening = false;
                    voiceBtn.classList.remove('listening');
                    searchInput.placeholder = 'Search services (e.g., Electrician, Taxi)...';
                };

                recognition.onerror = (event) => {
                    console.error('Speech recognition error:', event.error);
                    isListening = false;
                    voiceBtn.classList.remove('listening');
                    searchInput.placeholder = 'Search services (e.g., Electrician, Taxi)...';
                    
                    if (event.error === 'no-speech') {
                        alert('No speech detected. Please try again.');
                    } else if (event.error === 'not-allowed') {
                        alert('Microphone access denied. Please enable microphone permissions in your browser settings.');
                    } else if (event.error === 'network') {
                        alert('Network error. Please check your connection.');
                    }
                };

                recognition.onend = () => {
                    isListening = false;
                    voiceBtn.classList.remove('listening');
                    searchInput.placeholder = 'Search services (e.g., Electrician, Taxi)...';
                };
            } else {
                // Browser doesn't support speech recognition
                voiceBtn.disabled = true;
                voiceBtn.title = 'Voice search not supported in this browser';
                voiceBtn.style.opacity = '0.3';
            }
        }
    }
}

function initCategoryPage() {
    const params = new URLSearchParams(window.location.search);
    const catId = params.get('id');
    const container = document.getElementById('provider-list');
    const titleEl = document.getElementById('category-title');
    const searchInput = document.getElementById('search-input');

    if (!catId) {
        window.location.href = 'index.html';
        return;
    }

    const data = window.getProviders(catId);

    if (!data) {
        titleEl.textContent = 'Category Not Found';
        container.innerHTML = '<div class="empty-state">Category not found. <a href="index.html">Go Home</a></div>';
        return;
    }

    titleEl.textContent = `${data.icon} ${data.name}`;

    // SEO: Dynamic Title & Meta Description
    document.title = `${data.name} in Bhuj | Bhuj Online`;

    let metaDesc = document.querySelector('meta[name="description"]');
    if (!metaDesc) {
        metaDesc = document.createElement('meta');
        metaDesc.name = "description";
        document.head.appendChild(metaDesc);
    }
    metaDesc.content = `Find the best ${data.name} in Bhuj. Contact details for ${data.providers.length} providers like ${data.providers[0]?.name}.`;

    renderProviders(data.providers, container);

    // Search filter
    searchInput.addEventListener('focus', () => {
        if (window.innerWidth <= 600) {
            document.body.classList.add('search-active');
        }
    });

    searchInput.addEventListener('blur', () => {
        setTimeout(() => {
            document.body.classList.remove('search-active');
        }, 200);
    });

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        const filtered = data.providers.filter(p =>
            p.name.toLowerCase().includes(query) ||
            p.area.toLowerCase().includes(query) ||
            p.phone.includes(query)
        );
        renderProviders(filtered, container);
    });
}

function renderProviders(providers, container) {
    if (providers.length === 0) {
        container.innerHTML = '<div class="empty-state">No providers found.</div>';
        return;
    }

    const html = providers.map(p => {
        const tagsHtml = p.tags.map(t => {
            const className = t.toLowerCase().replace(/[^a-z0-9]/g, '');
            return `<span class="tag ${className}">${t}</span>`;
        }).join('');

        // Clean phone for WhatsApp (remove spaces, dashes)
        const cleanPhone = p.phone.replace(/\D/g, '');
        // Assume India code +91 if length is 10, otherwise just use number
        const waNumber = cleanPhone.length === 10 ? `91${cleanPhone}` : cleanPhone;

        return `
        <li class="provider-card">
            <div class="provider-header">
                <div class="provider-name">${p.name}</div>
                <div class="provider-area">${p.area}</div>
            </div>
            
            <div class="tags">${tagsHtml}</div>

            <div class="provider-actions">
                <a href="tel:${p.phone}" class="action-btn btn-call">
                    <span class="phone-icon">📞</span> ${p.phone}
                </a>
                <a href="https://wa.me/${waNumber}" target="_blank" class="action-btn btn-whatsapp">
                    💬 WhatsApp
                </a>
                ${p.webpage ? 
                    `<a href="${p.webpage}" target="_blank" class="action-btn btn-webpage">
                        🌐 Webpage
                    </a>` :
                    `<button class="action-btn btn-webpage btn-disabled" disabled>
                        🌐 Webpage
                    </button>`
                }
            </div>
        </li>
        `;
    }).join('');

    container.innerHTML = html;
}

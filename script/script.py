def check_AJAX():
    script = ("""
    (function() {
        const originalXhrOpen = XMLHttpRequest.prototype.open;
        const originalXhrSend = XMLHttpRequest.prototype.send;
        let activeRequests = 0;

        XMLHttpRequest.prototype.open = function() {
            activeRequests++;
            console.log('AJAX request started');
            return originalXhrOpen.apply(this, arguments);
        };

        XMLHttpRequest.prototype.send = function() {
            this.addEventListener('loadend', function() {
                activeRequests--;
                console.log('AJAX request completed');
            });
            return originalXhrSend.apply(this, arguments);
        };

        // Функция для проверки активных запросов
        window.checkActiveAjaxRequests = function() {
            return activeRequests;
        };

        // Проверка состояния каждые 1 секунды
        setInterval(() => {
            console.log('Active requests: ', activeRequests);
        }, 1000);
    })();
    """)
    return script

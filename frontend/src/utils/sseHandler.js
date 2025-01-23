class SSEHandler {
  constructor(url) {
    this.url = url;
    this.eventSource = null;
  }

  connect(onMessage, onError) {
    this.eventSource = new EventSource(this.url);

    this.eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      onMessage(data);
    };

    this.eventSource.onerror = (err) => {
      onError(err);
      this.eventSource.close();
    };
  }

  disconnect() {
    if (this.eventSource) {
      this.eventSource.close();
    }
  }
}

export default SSEHandler;

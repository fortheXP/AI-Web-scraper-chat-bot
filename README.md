# 🕷️ AI WebScraper Chat - Intelligent Web Content Q&A

<img width="1609" height="745" alt="image" src="https://github.com/user-attachments/assets/0d048eaf-0606-4640-81c2-34a01ae4a249" />

<img width="1239" height="756" alt="image" src="https://github.com/user-attachments/assets/13028acf-4209-4bd2-a11a-8ab282a3073c" />

<img width="1119" height="610" alt="image" src="https://github.com/user-attachments/assets/07c1a547-95f5-471e-80cf-3859754d1968" />

> An intelligent web scraping application that combines the power of LangChain, Ollama, and Streamlit to create an interactive Q&A system for any webpage content.

## ⚠️ Important Limitations

### Bot Detection & Anti-Scraping Measures
This is a **basic web crawler** designed for educational purposes and simple websites. It may encounter issues with:

- **Cloudflare Protection**: Sites using Cloudflare's bot detection will likely block requests
- **Rate Limiting**: Aggressive scraping may trigger IP-based restrictions  
- **JavaScript-Heavy Sites**: Complex SPAs may not render content properly with basic Selenium setup
- **CAPTCHA Systems**: Human verification systems will prevent automated access
- **Geo-blocking**: Region-restricted content may be inaccessible
- **Authentication**: Login-required pages are not supported

### Recommended Use Cases
- Personal blogs and documentation sites
- Simple news websites without heavy protection
- Educational and research websites
- Static content pages
- Testing and learning purposes

### Ethical Considerations
- Always respect `robots.txt` files
- Implement appropriate delays between requests
- Use responsibly and within website terms of service
- Consider reaching out to site owners for permission when scraping large amounts of data


## 🎯 Project Overview

This project demonstrates the integration of modern AI technologies to create a practical web scraping and question-answering system. Users can input any URL, and the application will crawl, index, and enable natural language queries about the content.

### Key Features

- 🌐 **Web Scraping**: Automated content extraction from any accessible webpage
- 🧠 **AI-Powered Q&A**: Natural language processing for intelligent question answering
- 📊 **Vector Search**: Semantic similarity search for relevant content retrieval
- 💬 **Interactive Chat**: Streamlit-based user interface for seamless interaction
- 🏠 **Local Processing**: Runs entirely on local infrastructure using Ollama

## 🛠️ Technology Stack

- **Frontend**: Streamlit for interactive web interface
- **LLM**: Ollama with Llama 3.2 model for text generation
- **Embeddings**: mxbai-embed-large for semantic text representation
- **Web Scraping**: Selenium WebDriver for dynamic content extraction
- **Vector Storage**: LangChain InMemoryVectorStore for document indexing
- **Text Processing**: RecursiveCharacterTextSplitter for content chunking

## 🏗️ Architecture

```
User Input (URL) → Selenium Scraper → Document Chunking → Vector Embeddings → Vector Store
                                                                                    ↓
User Question → Similarity Search ← Vector Store → Context Retrieval → LLM → Response
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- Ollama installed locally
- Chrome/Chromium browser (for Selenium)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ai-website-scraper
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up Ollama models**
   ```bash
   ollama pull llama3.2
   ollama pull mxbai-embed-large
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

### Usage

1. Enter a webpage URL in the input field
2. Wait for the application to crawl and index the content
3. Ask questions about the webpage content in natural language
4. Get AI-powered responses based on the scraped content

## 📁 Project Structure

```
ai-website-scraper/
├── main.py              # Main application file
├── pyproject.toml       # Project dependencies
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (if needed)
```

## 🔧 Technical Implementation

### Web Scraping Pipeline
- Uses Selenium WebDriver for JavaScript-heavy websites
- Implements RecursiveCharacterTextSplitter for optimal text chunking
- Handles dynamic content loading and modern web applications

### AI/ML Components
- **Embeddings Model**: mxbai-embed-large for high-quality text representations
- **Language Model**: Llama 3.2 for natural language understanding and generation
- **Vector Store**: In-memory storage for fast similarity searches
- **Retrieval System**: Semantic search for contextually relevant information

### User Experience
- Clean, intuitive Streamlit interface
- Real-time processing indicators
- Chat-like interaction pattern
- Error handling and user feedback

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- **Modern AI Frameworks**: LangChain for LLM orchestration
- **Local AI Deployment**: Ollama for privacy-focused AI applications
- **Web Technologies**: Selenium automation and dynamic content handling
- **Vector Databases**: Semantic search and retrieval systems
- **Full-Stack Development**: End-to-end application development
- **User Experience Design**: Creating intuitive AI interfaces

## 🚧 Future Enhancements

- [ ] **Multi-URL Support**: Crawl and index multiple websites simultaneously
- [ ] **Persistent Storage**: Add database support for session persistence
- [ ] **Advanced Scraping**: Support for authentication and complex site structures
- [ ] **Export Features**: Save conversations and extracted data
- [ ] **API Integration**: RESTful API for programmatic access
- [ ] **Performance Optimization**: Caching and background processing
- [ ] **Security Features**: Rate limiting and input validation
- [ ] **Analytics Dashboard**: Usage statistics and query insights

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Connect

Built as part of my AI learning journey. Connect with me on:
- LinkedIn: [Bharath](www.linkedin.com/in/bharath-m-440b1a130)
- GitHub: [@forthexp](https://github.com/forthexp)

---

*This project showcases the practical application of modern AI technologies in web scraping and natural language processing, demonstrating the integration of multiple cutting-edge tools to create a useful, real-world application.*

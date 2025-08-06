#!/bin/bash
# Dynamic AI Agent - Docker Entrypoint Script
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🤖 Dynamic AI Agent - Starting Container${NC}"

# Function to check if API keys are set
check_api_keys() {
    local missing_keys=()
    
    if [ -z "$GOOGLE_API_KEY" ]; then
        missing_keys+=("GOOGLE_API_KEY")
    fi
    
    if [ -z "$SERPER_API_KEY" ]; then
        missing_keys+=("SERPER_API_KEY")
    fi
    
    if [ ${#missing_keys[@]} -ne 0 ]; then
        echo -e "${YELLOW}⚠️  Warning: Missing API keys: ${missing_keys[*]}${NC}"
        echo -e "${YELLOW}   Some features may not work properly.${NC}"
        echo -e "${BLUE}   Please set the following environment variables:${NC}"
        for key in "${missing_keys[@]}"; do
            echo -e "${BLUE}   - $key${NC}"
        done
        echo ""
    else
        echo -e "${GREEN}✅ API keys configured${NC}"
    fi
}

# Function to run setup if needed
run_setup() {
    if [ "$RUN_SETUP" = "true" ] || [ ! -f "/app/.setup_complete" ]; then
        echo -e "${BLUE}🔧 Running initial setup...${NC}"
        python main.py setup
        touch /app/.setup_complete
        echo -e "${GREEN}✅ Setup complete${NC}"
    fi
}

# Function to validate configuration
validate_config() {
    if [ "$SKIP_VALIDATION" != "true" ]; then
        echo -e "${BLUE}🔍 Validating configuration...${NC}"
        if python main.py validate-config; then
            echo -e "${GREEN}✅ Configuration valid${NC}"
        else
            echo -e "${RED}❌ Configuration validation failed${NC}"
            if [ "$STRICT_VALIDATION" = "true" ]; then
                exit 1
            fi
        fi
    fi
}

# Function to run tests if requested
run_tests() {
    if [ "$RUN_TESTS" = "true" ]; then
        echo -e "${BLUE}🧪 Running tests...${NC}"
        python main.py test
        echo -e "${GREEN}✅ Tests completed${NC}"
    fi
}

# Function to generate diagrams if requested
generate_diagrams() {
    if [ "$GENERATE_DIAGRAMS" = "true" ]; then
        echo -e "${BLUE}📊 Generating flow diagrams...${NC}"
        python main.py visualize
        echo -e "${GREEN}✅ Diagrams generated${NC}"
    fi
}

# Main execution
main() {
    echo -e "${BLUE}Container started at $(date)${NC}"
    echo -e "${BLUE}Python version: $(python --version)${NC}"
    echo -e "${BLUE}Working directory: $(pwd)${NC}"
    echo ""
    
    # Check API keys
    check_api_keys
    
    # Run setup if needed
    run_setup
    
    # Validate configuration
    validate_config
    
    # Run tests if requested
    run_tests
    
    # Generate diagrams if requested
    generate_diagrams
    
    echo -e "${GREEN}🚀 Starting Dynamic AI Agent...${NC}"
    echo ""
    
    # Execute the main command
    exec "$@"
}

# Run main function with all arguments
main "$@"

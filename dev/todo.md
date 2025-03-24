# Vibe-coding-init-kit Implementation Plan

## Phase 1: Repository Structure Setup
- [x] Create dev folder for development documentation
- [x] Create main repository structure
  - [x] Setup src directory for source code
  - [x] Create templates directory for rule templates
  - [x] Setup tests directory
  - [x] Create examples directory
  - [x] Add LICENSE file
  - [x] Create README.md
  - [x] Add .gitignore

## Phase 2: Global and Project Rules Implementation
- [x] Design Global Rule structure
  - [x] Language settings templates
    - [x] Communication language settings
    - [x] Code comment language settings
  - [x] Global external library templates
- [x] Design Project Rule structure
  - [x] Project documentation templates
    - [x] Project content template
    - [x] TODO, goals, and progress tracking template
    - [x] Code documentation template
  - [x] Code writing requirements templates
    - [x] Clear commenting guidelines
    - [x] API-oriented coding style
    - [x] File length control guidelines
    - [x] Test file writing standards
  - [x] Local external library templates
  - [x] Figure out user is using windsurf or cursor(add a question), and then correspondingly write the rules to .cursorrules or .windsurfrules
  - [x] Create files: `dev/project_description.md`, `dev/todo.md`, `dev/code_docs.md`
  - [ ] Project rules adding:
    - [ ] self-reflection on the rules in the end of developing
    - [ ] self-testing (Experimental) for everything developing
      - [ ] this is risky for it will directly control the computer
        - [ ] Add rules: 1. create venv; --> this even can make it into a local manus

## *Phase 4: CLI Development
- [x] Design CLI command structure
- [x] Implement commands to find and modify .cursorrules/.windsurfrules files
- [x] Create shell integration for zsh/bash
- [x] Create initialization commands
- [x] Distinguish between global and project settings
  - [x] Global settings for Windsurf: ~/.codeium/windsurf-next/memories/global_rules.md
  - [x] Global settings for Cursor: ~/.cursorrules
  - [x] Project settings: .windsurfrules or .cursorrules in project directory
- [x] Simplify interactive prompts
- [ ] 优化回复
- [x] 加一个ASCII Badge（我来）
- [x] 当没有 `project_description.md` 时，通过用户输入创建，而后创建对应的 `todo.md`


## DEV TODO
- [ ] test cursor

## Phase 3: MCP Installation Automation (GLOBAL PART)
- [ ] Research MCP installation process
- [ ] Create script for automatic MCP installation
- [ ] Test MCP installation script
- [ ] Integrate MCP installation with CLI

## Phase 5: Testing and Documentation
- [ ] Write comprehensive tests
- [ ] Create documentation
- [ ] Add usage examples

## Phase 6: Packaging and Distribution
- [ ] Package the tool
- [ ] Setup distribution method
- [ ] Create release strategy

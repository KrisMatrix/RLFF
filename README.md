# Reinforcement Learning from Functional Feedback

## Summary 
This year at my workplace, we are converting a large MATLAB codebase to Java. This MATLAB codebase is also tightly coupled with PowerWorld. For this conversion project, my team is using Copilot and Claude Opus/Sonnect for conversion to Java. However, they are using the "spec-driven development" method, with AI via VS Code/GitHub Copilot, to convert the code. 

After some thought, I realized we could develop an agentic workflow using RAGs and MCPs to further automate this project. I wanted to develop a proof-of-concept. At home, however, I don't have access to PowerWorld or MATLAB as these require paid licenses. So instead, I created a Perl script and decided to develop a proof of concept that converted Perl code to Python.

![System diagram of a Reinforcement Learning from Functional Feedback system. It shows how Perl code can be converted into Python](perl2python_RAG_and_RLFF_Sys_Diagram.drawio.png)

This proof of concept uses Gemini AI and a simple Python MCP.

# Claude Code Channels — 让外部消息推送到运行中的 Claude Code 会话

- **来源**：http://xhslink.com/o/3hk6bgE4o0p
- **官方文档**：https://docs.anthropic.com/en/docs/claude-code/channels
- **日期**：2026-03-20
- **关联项目**：
  - `HandOff_HandOn/` — 移动端远程控制 Claude Code，Channels 是互补方案
  - `Skills-Factory/` — Channel 插件开发与 Skill 生态相关

## 总结

1. **Claude Code Channels** 是 Anthropic 新发布的 Research Preview 功能，允许通过 MCP 协议将外部消息（Telegram/Discord）推送到正在运行的 Claude Code 会话中
2. **核心用法**：`claude --channels discord telegram` 启动后，Claude Code 会监听来自这些平台的消息，收到后自动处理并回复
3. **安全机制**：每个 Channel 插件维护发送者白名单（allowlist），通过配对码（pairing code）绑定账号，未授权用户的消息被静默丢弃
4. **企业控制**：Team/Enterprise 计划默认关闭，需管理员在 Admin Settings 中启用 `channelsEnabled`
5. **与 HandOn 的关系**：这是官方提供的"从手机远程控制本地 Claude Code"方案，与我们的 HandOff/HandOn 架构形成互补——Channels 走 Telegram/Discord 推送事件，HandOn 走 CloudKit 原生通信

## 关联

### 与 HandOff_HandOn 项目

- **互补而非替代**：Channels 通过第三方平台（Telegram/Discord）中转，HandOn 通过 CloudKit 直连 macOS
- **优势对比**：
  - Channels：无需自建 App，开箱即用，但依赖第三方平台且延迟较高
  - HandOn：原生 Apple 生态，低延迟，但需维护 iOS/macOS 双端 App
- **潜在整合**：可以考虑为 HandOn 开发一个 Channel 插件，让 HandOn 也成为 Claude Code 的官方 Channel 之一

### 与 Skills-Factory 项目

- Channel 插件本质是 MCP Server，与 Skill 开发同属 Claude Code 扩展生态
- 官方插件仓库 `claude-plugins-official` 可作为 Skill 分发的参考模式

## 技术细节

### 快速开始

```bash
# 1. 需要 Bun 运行时
bun --version

# 2. 安装 Channel 插件（以 fakechat 为例）
# 在 Claude Code 中运行 /plugin install 命令

# 3. 启动时启用 Channels
claude --channels discord telegram

# 4. 配对绑定（以 Telegram 为例）
# - 在 BotFather 创建 bot，获取 token
# - 配置 token 保存到 .claude/channels/telegram/.env
# - 给 bot 发消息获取配对码
# - 在 Claude Code 中确认配对
```

### 工作流程（从图片分析）

1. 终端运行 `claude --channels discord telegram`
2. Claude Code 显示 "Listening for channel messages from: discord, telegram"
3. Claude Code 正常执行任务（如 `npm test`）
4. Discord 用户 "sibling" 发来消息 "is the build green yet?"
5. Claude Code 自动回复 Discord："Still running tests — ~2 min. I'll ping you when it's done."
6. Telegram 用户 "thariq" 发来消息 "ship it when green 🚀"
7. Claude Code 同时处理来自多个平台的消息

### 支持的 Channels

| Channel | 状态 | 插件源码 |
|---------|------|----------|
| Telegram | ✅ 已支持 | `claude-plugins-official/external_plugins/telegram` |
| Discord | ✅ 已支持 | `claude-plugins-official/external_plugins/discord` |
| Fakechat | ✅ Demo | localhost:8787 本地演示 |
| 自定义 | 🔧 可开发 | 参考 Channels Reference 文档 |

### 要求与限制

- 需要 Claude Code v2.1.80+
- 需要 claude.ai 登录（不支持 Console/API Key 认证）
- 需要 Bun 运行时
- Research Preview 阶段，仅允许 Anthropic 维护的白名单插件
- 自定义插件需用 `--dangerously-load-development-channels` 标志

## 小红书原文

Anthropic发布Claude Code Channel，允许使用MCP远程输入Claude Code session. 现在支持Telegram和Discord #vibecoding #个人开发者 #AI工具 #人工智能 #大模型

## 引用内容原文

见官方文档全文：https://docs.anthropic.com/en/docs/claude-code/channels

（官方文档已在上方"技术细节"部分整理归纳，完整原文可通过链接访问）

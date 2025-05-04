## mcp-basics
mcp serverのお試し

### mcp serverの登録
1. clineを開く
2. MCP Serversを開く
3. Edit Configuretaionを開く
4. 以下のjsonを貼り付ける
```
{
  "mcpServers": {
      "simple_calculator": {
          "disabled": false,
          "timeout": 60,
          "command": "/usr/local/bin/uv",
          "args": [
            "--directory",
            "/workspaces/mcp-basics",
            "run",
            "server.py"
          ],
          "transportType": "stdio"
      }
  }
}
```
5. 以下のプロンプトを実行してツールが使われるのを確認する
```
ツールを利用して123と456の積を計算して
```
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: EmailAnalyzer(),
    );
  }
}

class EmailAnalyzer extends StatefulWidget {
  @override
  _EmailAnalyzerState createState() => _EmailAnalyzerState();
}

class _EmailAnalyzerState extends State<EmailAnalyzer> {
  final TextEditingController _controller = TextEditingController();
  String _result = '';

  Future<void> analyzeEmail(String emailText) async {
    final url = Uri.parse('http://10.0.2.2:5001/analyze'); // emulator localhost
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: json.encode({'email_text': emailText}),
    );

    if (response.statusCode == 200) {
      setState(() {
        _result = json.decode(response.body)['result'];
      });
    } else {
      setState(() {
        _result = 'Error: ${response.statusCode}';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Email Analyzer')),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              decoration: InputDecoration(labelText: 'Enter email text'),
              maxLines: 5,
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: () => analyzeEmail(_controller.text),
              child: Text('Analyze'),
            ),
            SizedBox(height: 16),
            Text('Result: $_result'),
          ],
        ),
      ),
    );
  }
}

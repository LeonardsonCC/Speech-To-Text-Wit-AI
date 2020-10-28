# Speech to Text
An app to capture voice and, using [wit.ai](https://wit.ai), converts the words to text.

## Configuration
Located in config.ini file.
| Category | Name                  | Description                                         |
|----------|-----------------------|-----------------------------------------------------|
| WIT_AI   | API_ENDPOINT          | [wit.ai](https://wit.ai) endpoint to speech to text |
| WIT_AI   | ACCESS_TOKEN          | Access token for wit.ai API                         |
| TEXT     | FOLDER                | Folder where text files will be saved               |
| AUDIO    | CHANNELS              | Channels to audio record                            |
| AUDIO    | RATE                  | Rate of audio record                                |
| AUDIO    | CHUNK                 | Chunk of audio record                               |
| AUDIO    | THRESHOLD             | Threshold for silence check                         |
| AUDIO    | SILENCE_TIME_CHECKER  | Threshold for silence check                         |

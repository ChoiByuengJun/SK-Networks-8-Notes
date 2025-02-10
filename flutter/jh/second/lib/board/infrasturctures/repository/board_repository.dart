import 'package:second/board/domain/usecases/list/response/board_list_response.dart';

import '../../domain/entity/board.dart';

abstract class BoardRepository {
  Future<BoardListResponse> listBoard(int page, int perPage);
  Future<Board> create(String title, String content, String userToken);
}
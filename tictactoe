import javafx.application.Application;
import javafx.application.Platform;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.util.Random;

public class tictactoe extends Application {

    private char currentPlayer = 'X';
    private Button[][] board = new Button[3][3];
    private Label statusLabel = new Label("Player X's turn");
    private TextField playerXField = new TextField("Player X");
    private TextField playerOField = new TextField("Player O");
    private TextField gamesField = new TextField("1");
    private int playerXWins = 0;
    private int playerOWins = 0;
    private Label scoreLabel = new Label("Score: Player X 0 - Player O 0");
    private boolean singlePlayerMode = false;
    private Random random = new Random();
    private int totalGames = 1;
    private int gamesPlayed = 0;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Tic Tac Toe");

        VBox startScreen = new VBox(10);
        startScreen.setAlignment(Pos.CENTER);
        Button startButton = new Button("Player vs Player");
        startButton.setOnAction(e -> {
            singlePlayerMode = false; // Reset singlePlayerMode
            startGame(primaryStage);
        });
        Button startSinglePlayerButton = new Button("Player vs Computer");
        startSinglePlayerButton.setOnAction(e -> {
            singlePlayerMode = true;
            startGame(primaryStage);
        });
        Button quitButton = new Button("Quit");
        quitButton.setOnAction(e -> Platform.exit());

        startScreen.getChildren().addAll(
                new Label("Tic Tac Toe"),
                new Label("Number of Games:"),
                gamesField,
                startButton,
                startSinglePlayerButton,
                quitButton
        );

        Scene startScene = new Scene(startScreen, 300, 300);
        primaryStage.setScene(startScene);
        primaryStage.show();
    }

    private void startGame(Stage primaryStage) {
        try {
            totalGames = Integer.parseInt(gamesField.getText());
        } catch (NumberFormatException e) {
            totalGames = 1; // default to 1 game if invalid input
        }
        gamesPlayed = 0;
        playerXWins = 0;
        playerOWins = 0;
        updateScore();

        GridPane gridPane = new GridPane();
        gridPane.setAlignment(Pos.CENTER);
        gridPane.setHgap(10);
        gridPane.setVgap(10);

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                Button button = new Button();
                button.setMinSize(100, 100);
                button.setOnAction(e -> makeMove(button));
                board[i][j] = button;
                gridPane.add(button, j, i);
            }
        }

        Button menuButton = new Button("Menu");
        menuButton.setOnAction(e -> showStartScreen(primaryStage));

        VBox vbox = new VBox(10);
        vbox.setAlignment(Pos.CENTER);
        vbox.getChildren().addAll(
                new Label("Player X:"), playerXField,
                new Label("Player O:"), playerOField,
                statusLabel, gridPane, scoreLabel, menuButton
        );

        Scene gameScene = new Scene(vbox, 400, 500);
        primaryStage.setScene(gameScene);

        // Check if it's single-player mode and computer should start as 'O'
        if (singlePlayerMode && currentPlayer == 'O') {
            makeComputerMove();
        }
    }

    private void showStartScreen(Stage primaryStage) {
        primaryStage.setScene(new Scene(new VBox(10), 300, 300));
        start(primaryStage);
    }

    private void makeMove(Button button) {
        if (button.getText().isEmpty()) {
            button.setText(String.valueOf(currentPlayer));
            handleEndOfGame();
        }
    }

    private void makeComputerMove() {
        int row, col;
        do {
            row = random.nextInt(3);
            col = random.nextInt(3);
        } while (!board[row][col].getText().isEmpty());
        board[row][col].setText(String.valueOf(currentPlayer));
        handleEndOfGame();
    }

    private void handleEndOfGame() {
        if (checkWinner()) {
            statusLabel.setText("Player " + currentPlayer + " wins!");
            updateScoreAndGames();
        } else if (isBoardFull()) {
            statusLabel.setText("The game is a draw!");
            gamesPlayed++;
            if (gamesPlayed < totalGames) {
                resetBoard();
            } else {
                showFinalResult();
            }
        } else {
            switchPlayer();
            if (singlePlayerMode && currentPlayer == 'O') {
                makeComputerMove();
            }
        }
    }

    private void switchPlayer() {
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
        statusLabel.setText("Player " + currentPlayer + "'s turn");
    }

    private boolean checkWinner() {
        for (int i = 0; i < 3; i++) {
            if ((board[i][0].getText().equals(String.valueOf(currentPlayer)) &&
                    board[i][1].getText().equals(String.valueOf(currentPlayer)) &&
                    board[i][2].getText().equals(String.valueOf(currentPlayer))) ||
                    (board[0][i].getText().equals(String.valueOf(currentPlayer)) &&
                            board[1][i].getText().equals(String.valueOf(currentPlayer)) &&
                            board[2][i].getText().equals(String.valueOf(currentPlayer)))) {
                return true;
            }
        }
        return (board[0][0].getText().equals(String.valueOf(currentPlayer)) &&
                board[1][1].getText().equals(String.valueOf(currentPlayer)) &&
                board[2][2].getText().equals(String.valueOf(currentPlayer))) ||
                (board[0][2].getText().equals(String.valueOf(currentPlayer)) &&
                        board[1][1].getText().equals(String.valueOf(currentPlayer)) &&
                        board[2][0].getText().equals(String.valueOf(currentPlayer)));
    }

    private boolean isBoardFull() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j].getText().isEmpty()) {
                    return false;
                }
            }
        }
        return true;
    }

    private void updateScoreAndGames() {
        if (currentPlayer == 'X') {
            playerXWins++;
        } else {
            playerOWins++;
        }
        gamesPlayed++;
        updateScore();
        if (gamesPlayed < totalGames) {
            resetBoard();
        } else {
            showFinalResult();
        }
    }

    private void updateScore() {
        scoreLabel.setText("Score: " + playerXField.getText() + " " + playerXWins + " - " + playerOField.getText() + " " + playerOWins);
    }

    private void resetBoard() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j].setText("");
            }
        }
        currentPlayer = 'X';
        statusLabel.setText("Player " + currentPlayer + "'s turn");

        // Check if it's single-player mode and computer should start as 'O'
        if (singlePlayerMode && currentPlayer == 'O') {
            makeComputerMove();
        }
    }

    private void showFinalResult() {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Game Over");
        if (playerXWins > playerOWins) {
            alert.setHeaderText("Player " + playerXField.getText() + " wins the series!");
        } else if (playerOWins > playerXWins) {
            alert.setHeaderText("Player " + playerOField.getText() + " wins the series!");
        } else {
            alert.setHeaderText("The series is a draw!");
        }
        alert.setContentText("Final Score: " + playerXField.getText() + " " + playerXWins + " - " + playerOField.getText() + " " + playerOWins);
        alert.showAndWait();
        showStartScreen((Stage) statusLabel.getScene().getWindow());
    }
}

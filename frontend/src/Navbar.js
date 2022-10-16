import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import Button from "react-bootstrap/Button";

function BasicExample() {
  const handleLogOut = () => {
    localStorage.removeItem("userId");
    localStorage.removeItem("isAuthenticated");
    window.location.pathname = "/login";
  };

  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="/">Pattrn</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">Dashboard</Nav.Link>
            <Nav.Link href="/goals">Goals</Nav.Link>
            <Nav.Link href="/progress">Progress</Nav.Link>
          </Nav>
          <Button variant="danger" onClick={handleLogOut}>
            Log Out
          </Button>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default BasicExample;

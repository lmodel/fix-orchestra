package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One entry of a message's identifiers, a field carried over or a field set. It holds exactly one of these.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraIdentifiersMemberV10  {

  private OrchestraIdentifierV10 fixrCorrelate;
  private OrchestraIdentifierV10 fixrAssign;


}
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
  The fields a message sent by an action sets or carries over.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraIdentifiersV11  {

  private List<OrchestraIdentifiersMemberV11> fixrMembers;
  private OrchestraAnnotationV11 fixrAnnotation;


}
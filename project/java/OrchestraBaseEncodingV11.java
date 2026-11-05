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
  What every encoding block shares: notes, and XML in another namespace that says how an element is encoded.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class OrchestraBaseEncodingV11  {

  private OrchestraAnnotationV11 fixrAnnotation;
  private List<OrchestraXmlElement> fixrAny;


}